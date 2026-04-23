from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.core.roles import is_admin  # 🔥 async (Mongo)

router = Router()


# 🔘 MANAGER PANEL KEYBOARD
def manager_panel_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚫 BL-USER", callback_data="bl_user")],
        [InlineKeyboardButton(text="📢 BROADCAST", callback_data="broadcast")],
        [InlineKeyboardButton(text="👤 AUTH USERS", callback_data="auth_users")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="admin_panel")]
    ])


# 🧑‍💼 MANAGER PANEL HANDLER
@router.callback_query(lambda c: c.data == "manager_panel")
async def open_manager_panel(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    # 🔥 FIX: await async role check
    if not await is_admin(user_id):
        return await callback.answer("Access Denied ❌", show_alert=True)

    text = (
        "<blockquote>"
        "┌────── ˹ ᴍᴀɴᴀɢᴇʀ ᴘᴀɴᴇʟ ˼─── ⏤‌‌●\n"
        "┆🧑‍💼 ᴍᴀɴᴀɢᴇʀ ᴄᴏɴᴛʀᴏʟs\n"
        "└─────────────────────•\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "🚫 BL-USER → block/unblock users\n"
        "📢 BROADCAST → send message to users\n"
        "👤 AUTH USERS → manage access users\n"
        "</blockquote>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=manager_panel_kb(),
        parse_mode="HTML"
    )
