from aiogram import Router, types
from aiogram.filters import Command

from bot.core.roles import is_admin

router = Router()

# ⚠️ TEMP USER STORAGE (later move to DB)
USERS = set()


# 📌 SAVE USERS (call this in start.py also)
def add_user(user_id: int):
    USERS.add(user_id)


# 📌 BUTTON INFO
@router.callback_query(lambda c: c.data == "broadcast")
async def broadcast_info(callback: types.CallbackQuery):
    if not is_admin(callback.from_user.id):
        return await callback.answer("Access Denied ❌", show_alert=True)

    text = (
        "<blockquote>"
        "📢 BROADCAST SYSTEM\n\n"
        "Usage:\n"
        "/broadcast message\n"
        "OR reply to a message with /broadcast"
        "</blockquote>"
    )

    await callback.message.edit_text(text, parse_mode="HTML")


# 📢 BROADCAST COMMAND
@router.message(Command("broadcast"))
async def broadcast_message(message: types.Message):
    if not is_admin(message.from_user.id):
        return await message.reply("Not allowed ❌")

    # 📌 Get text
    text = None

    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    else:
        try:
            text = message.text.split(" ", 1)[1]
        except:
            return await message.reply("Usage: /broadcast message")

    success = 0
    failed = 0

    for user_id in USERS:
        try:
            await message.bot.send_message(user_id, text)
            success += 1
        except:
            failed += 1

    await message.reply(
        f"📢 Broadcast Done\n\n✅ Success: {success}\n❌ Failed: {failed}"
    )
