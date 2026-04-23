import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from bot.handlers.start import router as start_router

from bot.config import BOT_TOKEN

# 👉 import your routers
from handlers.start import router as start_router


# ==============================
# 🔧 LOGGING SETUP
# ==============================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)


# ==============================
# 🚀 MAIN FUNCTION
# ==============================
async def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing! Check your config or .env file.")

    # 🤖 Initialize bot
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

    # ⚙️ Dispatcher
    dp = Dispatcher()

    # 📦 Register routers
    dp.include_router(start_router)

    # 🧹 Delete webhook (important for polling)
    await bot.delete_webhook(drop_pending_updates=True)

    logging.info("🚀 Bot started successfully!")

    # ▶️ Start polling
    await dp.start_polling(bot)


# ==============================
# 🏁 ENTRY POINT
# ==============================
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("❌ Bot stopped.")
