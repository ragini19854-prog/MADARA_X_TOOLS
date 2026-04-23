from bot.config import OWNER_ID
from bot.database.db import managers_col

async def is_manager(user_id):
    user = await managers_col.find_one({"user_id": user_id})
    return user is not None

async def is_admin(user_id):
    return user_id == OWNER_ID or await is_manager(user_id)
