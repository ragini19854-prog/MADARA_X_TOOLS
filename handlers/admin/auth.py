from aiogram import Router, types
from aiogram.filters import Command

from bot.core.roles import is_admin  # 🔥 async
from bot.database.db import auth_col  # 🔥 MongoDB

router = Router()


# 📌 BUTTON INFO (UI)
@router.callback_query(lambda c: c.data == "auth_users")
async def auth_info(callback: types.CallbackQuery):
    if not await is_admin(callback.from_user.id):
        return await callback.answer("Access Denied ❌", show_alert=True)

    text = (
        "<blockquote>"
        "👤 AUTH USERS SYSTEM\n\n"
        "Commands:\n"
        "/auth user_id → add auth user\n"
        "/unauth user_id → remove auth user\n"
        "/authusers → list auth users"
        "</blockquote>"
    )

    await callback.message.edit_text(text, parse_mode="HTML")


# ➕ ADD AUTH USER
@router.message(Command("auth"))
async def add_auth_user(message: types.Message):
    if not await is_admin(message.from_user.id):
        return await message.reply("Not allowed ❌")

    try:
        user_id = int(message.text.split()[1])

        await auth_col.update_one(
            {"user_id": user_id},
            {"$set": {"user_id": user_id}},
            upsert=True
        )

        await message.reply(f"✅ User {user_id} added to auth users")

    except:
        await message.reply("Usage: /auth user_id")


# ➖ REMOVE AUTH USER
@router.message(Command("unauth"))
async def remove_auth_user(message: types.Message):
    if not await is_admin(message.from_user.id):
        return await message.reply("Not allowed ❌")

    try:
        user_id = int(message.text.split()[1])

        await auth_col.delete_one({"user_id": user_id})

        await message.reply(f"❌ User {user_id} removed from auth users")

    except:
        await message.reply("Usage: /unauth user_id")


# 📋 LIST AUTH USERS
@router.message(Command("authusers"))
async def list_auth_users(message: types.Message):
    if not await is_admin(message.from_user.id):
        return await message.reply("Not allowed ❌")

    users = []

    async for user in auth_col.find():
        users.append(str(user["user_id"]))

    if not users:
        return await message.reply("No auth users")

    await message.reply("👤 Auth Users:\n" + "\n".join(users))
