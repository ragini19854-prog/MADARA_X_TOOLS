from aiogram import Router, types
from aiogram.filters import Command

from bot.core.roles import is_admin
from bot.config import BLOCKED_USERS

router = Router()


# 📌 BUTTON CLICK (INFO)
@router.callback_query(lambda c: c.data == "bl_user")
async def bl_user_info(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    if not is_admin(user_id):
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
    user_id = message.from_user.id

    if not is_admin(user_id):
        return await message.reply("Not allowed ❌")

    try:
        target_id = int(message.text.split()[1])
        BLOCKED_USERS.add(target_id)

        await message.reply(f"User {target_id} blocked 🚫")

    except:
        await message.reply("Usage: /block user_id")


# 🔓 UNBLOCK USER
@router.message(Command("unblock"))
async def unblock_user(message: types.Message):
    user_id = message.from_user.id

    if not is_admin(user_id):
        return await message.reply("Not allowed ❌")

    try:
        target_id = int(message.text.split()[1])
        BLOCKED_USERS.discard(target_id)

        await message.reply(f"User {target_id} unblocked ✅")

    except:
        await message.reply("Usage: /unblock user_id")


# 📋 LIST BLOCKED USERS
@router.message(Command("blockedusers"))
async def list_blocked(message: types.Message):
    user_id = message.from_user.id

    if not is_admin(user_id):
        return await message.reply("Not allowed ❌")

    if not BLOCKED_USERS:
        return await message.reply("No blocked users")

    users = "\n".join(str(uid) for uid in BLOCKED_USERS)

    await message.reply(f"🚫 Blocked Users:\n{users}")
