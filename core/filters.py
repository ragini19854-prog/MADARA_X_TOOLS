from bot.database.db import blocked_col

async def is_blocked(user_id):
    user = await blocked_col.find_one({"user_id": user_id})
    return user is not None
