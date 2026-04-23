import os
from dotenv import load_dotenv

load_dotenv()


# ==============================
# 🤖 BOT CONFIG
# ==============================

BOT_TOKEN = os.getenv("BOT_TOKEN")

# 👑 Owner
OWNER_ID = int(os.getenv("OWNER_ID", "0"))


# ==============================
# 👥 ROLE SYSTEM
# ==============================

# Managers (can use admin panel but NOT add managers)
MANAGERS = set(map(int, os.getenv("MANAGERS", "").split())) if os.getenv("MANAGERS") else set()

# Auth users (temporary elevated access)
AUTH_USERS = set(map(int, os.getenv("AUTH_USERS", "").split())) if os.getenv("AUTH_USERS") else set()


# ==============================
# 🚫 SECURITY SYSTEM
# ==============================

# Blocked users (blacklist)
BLOCKED_USERS = set()


# ==============================
# 💎 PREMIUM SYSTEM
# ==============================

# Default limits
FREE_DAILY_LIMIT = 5

# Premium users storage (user_id: expiry_timestamp)
PREMIUM_USERS = {}


# ==============================
# ⚡ QUEUE SYSTEM
# ==============================

# Task queue
TASK_QUEUE = []

# Max concurrent tasks
MAX_WORKERS = 2


# ==============================
# 🌐 LINKS (EDIT THESE)
# ==============================

CHANNEL_LINK = "https://t.me/+Imyf3M9TO5k1ODRl"
GROUP_LINK = "https://t.me/+dv_rcq5uIXhmMWM1"
DEVELOPER_LINK = "https://t.me/YOUR_MADARA_BRO"

PAYMENT_CONTACT = "@MADARA_X_HELPER_bot"


# ==============================
# ⚙️ FEATURE TOGGLES
# ==============================

ENABLE_BG_REMOVE = True
ENABLE_DOWNLOADER = True
ENABLE_CONVERTER = True
ENABLE_UPLOADER = True
ENABLE_YT_TEXT = True


# ==============================
# 🧠 HELPER FUNCTIONS
# ==============================

def is_owner(user_id: int) -> bool:
    return user_id == OWNER_ID


def is_manager(user_id: int) -> bool:
    return user_id in MANAGERS


def is_admin(user_id: int) -> bool:
    return is_owner(user_id) or is_manager(user_id)


def is_blocked(user_id: int) -> bool:
    return user_id in BLOCKED_USERS


def is_premium(user_id: int) -> bool:
    import time
    expiry = PREMIUM_USERS.get(user_id)
    return expiry and expiry > time.time()
