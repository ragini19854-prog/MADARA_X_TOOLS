from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config import OWNER_ID

router = Router()


# 🔘 OWNER PANEL KEYBOARD
def owner_panel_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚫 BL-USER", callback_data="bl_user")],
        [InlineKeyboardButton(text="📢 BROADCAST", callback_data="broadcast")],
        [InlineKeyboardButton(text="➕ ADD MANAGER", callback_data="add_manager")],
        [InlineKeyboardButton(text="💎 ADD PREMIUM", callback_data="add_premium")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="admin_panel")]
    ])


# 👑 OWNER PANEL HANDLER
@router.callback_query(lambda c: c.data == "owner_panel")
async def open_owner_panel(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    if user_id != OWNER_ID:
        return await callback.answer("Only Owner Allowed ❌", show_alert=True)

    text = (
        "<blockquote>"
        "┌────── ˹ ᴏᴡɴᴇʀ ᴘᴀɴᴇʟ ˼─── ⏤‌‌●\n"
        "┆👑 ғᴜʟʟ ᴄᴏɴᴛʀᴏʟ ᴄᴇɴᴛᴇʀ\n"
        "└─────────────────────•\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "🚫 BL-USER → block/unblock users\n"
        "📢 BROADCAST → send message to all\n"
        "➕ ADD MANAGER → manage admins\n"
        "💎 ADD PREMIUM → give premium access\n"
        "</blockquote>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=owner_panel_kb(),
        parse_mode="HTML"
    )
