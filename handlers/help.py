from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.roles import is_admin

router = Router()


# 🔘 HELP KEYBOARD
def help_keyboard(is_admin_user=False):
    buttons = [
        [InlineKeyboardButton(text="🖼 Background Remover", callback_data="bg_remove")],
        [InlineKeyboardButton(text="📥 Downloader", callback_data="downloader")],
        [InlineKeyboardButton(text="🔗 Image to Link", callback_data="img_link")],
        [InlineKeyboardButton(text="📄 File Converter", callback_data="converter")],
        [InlineKeyboardButton(text="🎧 YouTube to Text", callback_data="yt_text")],
        [InlineKeyboardButton(text="💎 Premium", callback_data="premium")]
    ]

    if is_admin_user:
        buttons.append(
            [InlineKeyboardButton(text="⚙️ Admin Panel", callback_data="admin_panel")]
        )

    buttons.append(
        [InlineKeyboardButton(text="🔙 Back", callback_data="back_start")]
    )

    return InlineKeyboardMarkup(inline_keyboard=buttons)


# 📘 HELP MENU CALLBACK
@router.callback_query(lambda c: c.data == "help")
async def help_menu(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    text = (
        "<blockquote>"
        "┌────── ˹ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅ ˼─── ⏤‌‌●\n"
        "┆📘 ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴏᴏʟs ʙᴇʟᴏᴡ 👇\n"
        "└─────────────────────•\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "🖼 ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇʀ → ʀᴇᴍᴏᴠᴇ ɪᴍᴀɢᴇ ʙɢ\n"
        "📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ → ɪɴsᴛᴀ / ʏᴛ ᴅᴏᴡɴʟᴏᴀᴅ\n"
        "🔗 ɪᴍᴀɢᴇ ᴛᴏ ʟɪɴᴋ → ᴄʀᴇᴀᴛᴇ ᴘᴜʙʟɪᴄ ʟɪɴᴋ\n"
        "📄 ғɪʟᴇ ᴄᴏɴᴠᴇʀᴛᴇʀ → ᴘᴅғ / ᴡᴏʀᴅ / ᴘᴘᴛ\n"
        "🎧 ʏᴏᴜᴛᴜʙᴇ → ᴛᴇxᴛ → ᴇxᴛʀᴀᴄᴛ sᴄʀɪᴘᴛ\n"
        "💎 ᴘʀᴇᴍɪᴜᴍ → ᴜɴʟᴏᴄᴋ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "⚡ ᴄʟɪᴄᴋ ᴀɴʏ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴜsᴇ ғᴇᴀᴛᴜʀᴇ\n"
        "</blockquote>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=help_keyboard(is_admin(user_id)),
        parse_mode="HTML"
    )


# 🔙 BACK TO START
@router.callback_query(lambda c: c.data == "back_start")
async def back_start(callback: types.CallbackQuery):
    from handlers.start import start_keyboard  # avoid circular import

    user = callback.from_user.first_name

    text = (
        "<blockquote>"
        "┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼─── ⏤‌‌●\n"
        f"┆👋 ʜᴇʏ, <b>{user}</b> 🌸\n"
        "┆🤖 ᴡᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ 🚀\n"
        "└─────────────────────•\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "⚡ sᴇʟᴇᴄᴛ ᴀɴ ᴏᴘᴛɪᴏɴ ғʀᴏᴍ ʙᴇʟᴏᴡ 👇\n"
        "</blockquote>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=start_keyboard(),
        parse_mode="HTML"
    )
