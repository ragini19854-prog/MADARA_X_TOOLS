from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import PAYMENT_CONTACT

router = Router()


# 🔘 PREMIUM PLANS KEYBOARD
def premium_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💎 1 Day - ₹10", callback_data="plan_1")],
        [InlineKeyboardButton(text="💎 2 Days - ₹15", callback_data="plan_2")],
        [InlineKeyboardButton(text="💎 7 Days - ₹50", callback_data="plan_7")],
        [InlineKeyboardButton(text="💎 30 Days - ₹150", callback_data="plan_30")],
        [InlineKeyboardButton(text="🔙 Back", callback_data="help")]
    ])


# 💎 PREMIUM MENU
@router.callback_query(lambda c: c.data == "premium")
async def premium_menu(callback: types.CallbackQuery):

    text = (
        "<blockquote>"
        "┌────── ˹ ᴘʀᴇᴍɪᴜᴍ ˼─── ⏤‌‌●\n"
        "┆💎 ᴜɴʟᴏᴄᴋ ᴘᴏᴡᴇʀғᴜʟ ғᴇᴀᴛᴜʀᴇs 🚀\n"
        "└─────────────────────•\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "✨ ᴘʀᴇᴍɪᴜᴍ ʙᴇɴᴇғɪᴛs:\n"
        "⚡ ᴜɴʟɪᴍɪᴛᴇᴅ ᴜsᴀɢᴇ\n"
        "🚀 ғᴀsᴛᴇʀ sᴘᴇᴇᴅ\n"
        "📌 ᴘʀɪᴏʀɪᴛʏ ǫᴜᴇᴜᴇ\n"
        "🛠 ᴀʟʟ ᴛᴏᴏʟs ᴜɴʟᴏᴄᴋᴇᴅ\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "💳 sᴇʟᴇᴄᴛ ᴀ ᴘʟᴀɴ ʙᴇʟᴏᴡ 👇"
        "</blockquote>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=premium_kb(),
        parse_mode="HTML"
    )


# 💳 PLAN CLICK HANDLER
@router.callback_query(lambda c: c.data.startswith("plan_"))
async def select_plan(callback: types.CallbackQuery):

    plan = callback.data.split("_")[1]

    text = (
        "<blockquote>"
        "┌────── ˹ ᴘᴀʏᴍᴇɴᴛ ˼─── ⏤‌‌●\n"
        f"┆💎 sᴇʟᴇᴄᴛᴇᴅ ᴘʟᴀɴ: {plan} ᴅᴀʏ(s)\n"
        "└─────────────────────•\n"
        "</blockquote>\n\n"

        "<blockquote>"
        "💳 ᴄᴏᴍᴘʟᴇᴛᴇ ᴘᴀʏᴍᴇɴᴛ & sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ 👇\n\n"
        f"👤 ᴄᴏɴᴛᴀᴄᴛ: {PAYMENT_CONTACT}\n"
        "</blockquote>"
    )

    await callback.message.edit_text(
        text,
        parse_mode="HTML"
    )
