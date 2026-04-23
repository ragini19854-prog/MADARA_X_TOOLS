from aiogram import Router, types
from aiogram.filters import Command

from bot.core.roles import is_admin  # 🔥 async
from bot.database.db import blocked_col  # 🔥 MongoDB

router = Router()


# 📌 BUTTON CLICK (INFO)
@router.callback_query(lambda c: c.data == "bl_user")
async def bl_user_info(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    if not await is_admin(user_id):
        return await callback.answer("Access Denied ❌", show_alert=True)

    text = (
        "<blockquote>"
        "🚫 BL-USER SYSTEM\n\n"
        "Commands:\n"
        "/block user_id → block user\n"
        "/unblock user_id → unblock user\n"
        "/blockedusers → list blocked users"
        "</blockquote>"
    )

    await callback.message.edit_text(text, parse_mode="HTML")


# 🚫 BLOCK USER
@router.message(Command("block"))
async def block_user(message: types.Message):
    if not await is_admin(message.from_user.id):
        return await message.reply("Not allowed ❌")

    try:
        target_id = int(message.text.split()[1])

        # 🔥 store in MongoDB
        await blocked_col.update_one(
            {"user_id": target_id},
            {"$set": {"user_id": target_id}},
            upsert=True
        )

        await message.reply(f"🚫 User {target_id} blocked")

    except:
        await message.reply("Usage: /block user_id")


# 🔓 UNBLOCK USER
@router.message(Command("unblock"))
async def unblock_user(message: types.Message):
    if not await is_admin(message.from_user.id):
        return await message.reply("Not allowed ❌")

    try:
        target_id = int(message.text.split()[1])

        # 🔥 remove from MongoDB
        await blocked_col.delete_one({"user_id": target_id})

        await message.reply(f"✅ User {target_id} unblocked")

    except:
        await message.reply("Usage: /unblock user_id")


# 📋 LIST BLOCKED USERS
@router.message(Command("blockedusers"))
async def list_blocked(message: types.Message):
    if not await is_admin(message.from_user.id):
        return await message.reply("Not allowed ❌")

    users = []

    # 🔥 fetch from MongoDB
    async for user in blocked_col.find():
        users.append(str(user["user_id"]))

    if not users:
        return await message.reply("No blocked users")

    await message.reply("🚫 Blocked Users:\n" + "\n".join(users))
