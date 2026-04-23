from aiogram import Router, types
from aiogram.filters import Command

from bot.config import OWNER_ID
from bot.core.premium import add_premium

router = Router()


@router.message(Command("addpremium"))
async def add_premium_cmd(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("Only Owner ❌")

    try:
        _, days, user_id = message.text.split()
        days = int(days)
        user_id = int(user_id)

        add_premium(user_id, days)

        await message.reply(f"✅ Premium added for {days} days")

    except:
        await message.reply("Usage: /addpremium days user_id")
