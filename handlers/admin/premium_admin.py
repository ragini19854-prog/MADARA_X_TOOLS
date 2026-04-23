from aiogram import Router, types
from aiogram.filters import Command
import time

from bot.config import OWNER_ID
from bot.database.db import premium_col  # 🔥 MongoDB

router = Router()


@router.message(Command("addpremium"))
async def add_premium_cmd(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("Only Owner ❌")

    try:
        _, days, user_id = message.text.split()
        days = int(days)
        user_id = int(user_id)

        # ⏳ calculate expiry
        expiry = time.time() + (days * 86400)

        # 🔥 store in MongoDB
        await premium_col.update_one(
            {"user_id": user_id},
            {"$set": {"expiry": expiry}},
            upsert=True
        )

        await message.reply(f"💎 Premium added for {days} days")

    except:
        await message.reply("Usage: /addpremium days user_id")
