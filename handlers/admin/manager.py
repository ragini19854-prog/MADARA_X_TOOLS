from aiogram import Router, types
from aiogram.filters import Command

from bot.config import OWNER_ID
from bot.database.db import managers_col  # 🔥 MongoDB

router = Router()


# 📌 BUTTON INFO (UI)
@router.callback_query(lambda c: c.data == "add_manager")
async def manager_info(callback: types.CallbackQuery):
    if callback.from_user.id != OWNER_ID:
        return await callback.answer("Only Owner ❌", show_alert=True)

    text = (
        "<blockquote>"
        "➕ MANAGER SYSTEM\n\n"
        "Commands:\n"
        "/addmanager user_id → add manager\n"
        "/removemanager user_id → remove manager\n"
        "/managers → list managers"
        "</blockquote>"
    )

    await callback.message.edit_text(text, parse_mode="HTML")


# ➕ ADD MANAGER
@router.message(Command("addmanager"))
async def add_manager(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("Only Owner ❌")

    try:
        user_id = int(message.text.split()[1])

        await managers_col.update_one(
            {"user_id": user_id},
            {"$set": {"user_id": user_id}},
            upsert=True
        )

        await message.reply(f"✅ User {user_id} added as manager")

    except:
        await message.reply("Usage: /addmanager user_id")


# ➖ REMOVE MANAGER
@router.message(Command("removemanager"))
async def remove_manager(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("Only Owner ❌")

    try:
        user_id = int(message.text.split()[1])

        await managers_col.delete_one({"user_id": user_id})

        await message.reply(f"❌ User {user_id} removed from managers")

    except:
        await message.reply("Usage: /removemanager user_id")


# 📋 LIST MANAGERS
@router.message(Command("managers"))
async def list_managers(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("Only Owner ❌")

    users = []

    async for user in managers_col.find():
        users.append(str(user["user_id"]))

    if not users:
        return await message.reply("No managers added")

    await message.reply("👑 Managers:\n" + "\n".join(users))
