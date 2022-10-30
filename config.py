## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCXDPSuvTHziNvXeN5Ii3fW1wOoaujJpa1JIFP5WTYDhoud-W0P6TtpvUr7PdCYdzfbkr8haaC9qGL2ChB-mDUMqGcAYilhv8fVr94HBHPp-uL3eNyU4o4uKLWgOyZdQujtWoGrQNfHccz1zAD-9ldBNGnBI7LjS4eRvWEdZ24GDBUFLy1OLAQHbTz3WnYw_Q7WcVpy6vkKsSnOKeKu8g1HdD-wnH__hI1POGNJJmTlNIV1cNfOcN4gWgOFmkyYRemB7tYpavASpNxUirAan56i5U9ynIRxxfCCgkk1VbTm_Ez-Ph7Xhq7OgXwka8CtWrzPyYchhgH68RnxRwsRDwPOAAAAAVRi_IAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5719110483:AAGaUDt9Ryp8-xTNPzHa-LuQ9rDbsIF9oXA")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ipiiii")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "MusicTxnBot")
OWNER_ID = getenv("OWNER_ID", "1854384004")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Gooo2bot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xl444")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
