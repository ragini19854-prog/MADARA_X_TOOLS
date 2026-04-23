from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.core.roles import is_admin

router = Router()


def admin_panel_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🧑‍💼 MANAGER PANEL", callback_data="manager_panel")],
        [InlineKeyboardButton(text="👑 OWNER PANEL", callback_data="owner_panel")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="help")]
    ])


@router.callback_query(lambda c: c.data == "admin_panel")
async def open_admin_panel(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    if not is_admin(user_id):
        return await callback.answer("Access Denied ❌", show_alert=True)

    text = (
        "<blockquote>"
        "┌────── ˹ ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ ˼─── ⏤‌‌●\n"
        "┆⚙️ ᴀᴅᴍɪɴ ᴄᴏɴᴛʀᴏʟ ᴄᴇɴᴛᴇʀ\n"
        "└─────────────────────•\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "🧑‍💼 Manager Panel → basic controls\n"
        "👑 Owner Panel → full control\n"
        "</blockquote>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=admin_panel_kb(),
        parse_mode="HTML"
    )
