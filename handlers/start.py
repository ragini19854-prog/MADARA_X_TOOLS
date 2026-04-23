from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config import OWNER_ID
from bot.core.roles import is_admin
from bot.database.db import users_col  # 🔥 MongoDB

router = Router()


# 🔘 START KEYBOARD
def start_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📢 CHANNEL", url="https://t.me/yourchannel"),
            InlineKeyboardButton(text="👥 GROUP", url="https://t.me/yourgroup")
        ],
        [
            InlineKeyboardButton(text="👨‍💻 DEVELOPER", url="https://t.me/yourusername")
        ],
        [
            InlineKeyboardButton(text="💎 PREMIUM", callback_data="premium")
        ],
        [
            InlineKeyboardButton(text="📘 HELP AND COMMAND", callback_data="help")
        ]
    ])


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

    return InlineKeyboardMarkup(inline_keyboard=buttons)


# 🔘 ADMIN PANEL
def admin_panel_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🧑‍💼 MANAGER PANEL", callback_data="manager_panel")],
        [InlineKeyboardButton(text="👑 OWNER PANEL", callback_data="owner_panel")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="help")]
    ])


# 🔘 MANAGER PANEL
def manager_panel_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚫 BL-USER", callback_data="bl_user")],
        [InlineKeyboardButton(text="📢 BROADCAST", callback_data="broadcast")],
        [InlineKeyboardButton(text="👤 AUTH USERS", callback_data="auth_users")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="admin_panel")]
    ])


# 🔘 OWNER PANEL
def owner_panel_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚫 BL-USER", callback_data="bl_user")],
        [InlineKeyboardButton(text="📢 BROADCAST", callback_data="broadcast")],
        [InlineKeyboardButton(text="➕ ADD MANAGER", callback_data="add_manager")],
        [InlineKeyboardButton(text="💎 ADD PREMIUM", callback_data="add_premium")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="admin_panel")]
    ])


# 🚀 START COMMAND (MONGODB CONNECTED)
@router.message(CommandStart())
async def start_cmd(message: types.Message):
    user_id = message.from_user.id
    user = message.from_user.first_name

    # 🔥 SAVE USER IN MONGODB
    await users_col.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "user_id": user_id,
                "name": user
            }
        },
        upsert=True
    )

    text = (
        "<blockquote>"
        "┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼─── ⏤‌‌●\n"
        f"┆👋 ʜᴇʏ, <b>{user}</b> 🌸\n"
        "┆🤖 ɪ ᴀᴍ <b>ᴍᴜʟᴛɪ ᴜᴛɪʟɪᴛʏ ʙᴏᴛ</b> 🚀\n"
        "└─────────────────────•\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "✨ ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴀʟʟ-ɪɴ-ᴏɴᴇ ᴛᴏᴏʟ ʙᴏᴛ 😎\n"
        "🎯 ᴜsᴇ ᴍᴇ ғᴏʀ ᴅᴀɪʟʏ ᴛᴀsᴋs ⚡\n\n"
        "┌────── ˹ ғᴇᴀᴛᴜʀᴇs ˼ ─── ⏤‌‌●\n"
        "┆🖼 ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴇᴍᴏᴠᴇʀ\n"
        "┆📥 ᴅᴏᴡɴʟᴏᴀᴅᴇʀ\n"
        "┆🔗 ɪᴍᴀɢᴇ → ʟɪɴᴋ\n"
        "┆📄 ғɪʟᴇ ᴄᴏɴᴠᴇʀᴛᴇʀ\n"
        "┆🎧 ʏᴏᴜᴛᴜʙᴇ → ᴛᴇxᴛ\n"
        "┆💎 ᴘʀᴇᴍɪᴜᴍ\n"
        "└─────────────────────•"
        "</blockquote>\n\n"

        "<blockquote>"
        "⚡ ɴᴀᴠɪɢᴀᴛᴇ ᴜsɪɴɢ ʙᴜᴛᴛᴏɴs 👇\n"
        "💡 ᴜsᴇ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅ\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "👑 ᴘᴏᴡᴇʀᴇᴅ ʙʏ » | 𝐌 ᴀ ᴅ ᴀ ʀ ᴀ |\n"
        "🔗 @YOUR_MADARA_BRO"
        "</blockquote>"
    )

    await message.answer(
        text,
        reply_markup=start_keyboard(),
        parse_mode="HTML"
    )


# 📘 HELP CALLBACK
@router.callback_query(lambda c: c.data == "help")
async def help_menu(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    text = (
        "<b>📘 Help & Commands</b>\n\n"
        "Select any tool below to use:\n\n"
        "🖼 Background Remover\n"
        "📥 Downloader\n"
        "🔗 Image to Link\n"
        "📄 File Converter\n"
        "🎧 YouTube to Text\n"
        "💎 Premium"
    )

    await callback.message.edit_text(
        text,
        reply_markup=help_keyboard(await is_admin(user_id))  # 🔥 async ready
    )


# ⚙️ ADMIN PANEL
@router.callback_query(lambda c: c.data == "admin_panel")
async def admin_panel(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    if not await is_admin(user_id):
        return await callback.answer("Access Denied ❌", show_alert=True)

    text = "<b>⚙️ Admin Panel</b>\n\nChoose a panel below:"

    await callback.message.edit_text(text, reply_markup=admin_panel_kb())


# 🧑‍💼 MANAGER PANEL
@router.callback_query(lambda c: c.data == "manager_panel")
async def manager_panel(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    if not await is_admin(user_id):
        return await callback.answer("Access Denied ❌", show_alert=True)

    text = (
        "<b>🧑‍💼 Manager Panel</b>\n\n"
        "🚫 BL-USER\n📢 BROADCAST\n👤 AUTH USERS"
    )

    await callback.message.edit_text(text, reply_markup=manager_panel_kb())


# 👑 OWNER PANEL
@router.callback_query(lambda c: c.data == "owner_panel")
async def owner_panel(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    if user_id != OWNER_ID:
        return await callback.answer("Only Owner ❌", show_alert=True)

    text = (
        "<b>👑 Owner Panel</b>\n\n"
        "🚫 BL-USER\n📢 BROADCAST\n"
        "➕ ADD MANAGER\n💎 ADD PREMIUM"
    )

    await callback.message.edit_text(text, reply_markup=owner_panel_kb())
