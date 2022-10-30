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
BOT_NAME = getenv("BOT_NAME", "𝗞𝗼𝗖𝗵𝗶𝗸𝗶")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "akeen")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ipiiii")
ALIVE_NAME = getenv("ALIVE_NAME", "akeen")
BOT_USERNAME = getenv("BOT_USERNAME", "MusicTxnBot")
OWNER_ID = getenv("OWNER_ID", "5186954055")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Gooo2bot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Mus_3b2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "iPiiii")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5186954055").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/39c6305b5de327544264a.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/c692fa005018431294e91.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Akeen-T/uiii")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/b96757b04e6aeb6e5e069.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/6dbc099e85a19017bfd20.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/8cd16c476ff66c580a3ce.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/b12b2e70fbe208b34de2d.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/360529897cd53fc8d2c01.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/49b677c39b29994da0c68.jpg")
