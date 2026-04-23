import time

# user_id: expiry_timestamp
PREMIUM_USERS = {}


def add_premium(user_id: int, days: int):
    expiry = time.time() + (days * 86400)
    PREMIUM_USERS[user_id] = expiry


def is_premium(user_id: int) -> bool:
    expiry = PREMIUM_USERS.get(user_id)
    if not expiry:
        return False

    if expiry < time.time():
        PREMIUM_USERS.pop(user_id, None)
        return False

    return True


def get_remaining_days(user_id: int):
    expiry = PREMIUM_USERS.get(user_id)
    if not expiry:
        return 0

    remaining = expiry - time.time()
    return int(remaining // 86400)
