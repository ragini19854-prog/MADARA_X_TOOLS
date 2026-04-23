import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from bot.config import BOT_TOKEN

# 🔥 IMPORT ALL ROUTERS

# core handlers
from bot.handlers.start import router as start_router
from bot.handlers.help import router as help_router
from bot.handlers.premium import router as premium_router

# admin system
from bot.handlers.admin.admin_panel import router as admin_panel_router
from bot.handlers.admin.manager_panel import router as manager_panel_router
from bot.handlers.admin.owner_panel import router as owner_panel_router

from bot.handlers.admin.blacklist import router as blacklist_router
from bot.handlers.admin.broadcast import router as broadcast_router
from bot.handlers.admin.auth import router as auth_router
from bot.handlers.admin.manager import router as manager_router
from bot.handlers.admin.premium_admin import router as premium_admin_router

# (optional future tools)
# from bot.handlers.tools.bg_remove import router as bg_router
# from bot.handlers.tools.downloader import router as downloader_router


# ==============================
# 🔧 LOGGING
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
        raise ValueError("BOT_TOKEN missing in config")

    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # ==============================
    # 📦 REGISTER ROUTERS
    # ==============================

    # basic
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(premium_router)

    # admin panels
    dp.include_router(admin_panel_router)
    dp.include_router(manager_panel_router)
    dp.include_router(owner_panel_router)

    # admin features
    dp.include_router(blacklist_router)
    dp.include_router(broadcast_router)
    dp.include_router(auth_router)
    dp.include_router(manager_router)
    dp.include_router(premium_admin_router)

    # tools (later)
    # dp.include_router(bg_router)
    # dp.include_router(downloader_router)

    # ==============================
    # 🔄 START BOT
    # ==============================

    await bot.delete_webhook(drop_pending_updates=True)

    logging.info("🚀 Bot started successfully!")

    await dp.start_polling(bot)


# ==============================
# 🏁 ENTRY POINT
# ==============================
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("❌ Bot stopped.")
