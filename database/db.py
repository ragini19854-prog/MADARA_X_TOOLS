from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client["telegram_bot"]


# Collections
users_col = db["users"]
premium_col = db["premium"]
managers_col = db["managers"]
blocked_col = db["blocked"]
auth_col = db["auth"]
