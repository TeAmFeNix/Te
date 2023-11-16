## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBo9eAgsOoyDJf_AsoS6ouEdOPivBYj-5sGRBVLEPqx6KLsiw-3FSF8Oak8v16OTRuiIuCxuQ73qrsCrbb68TOCv5V2LZD53deNDIHXSFVRLZpE1qgufVn7epQk8RXolOapVJMkUXKcumuI7s1gyE25lixeJ7gqFK2HL8u7stYP8Re5J-e7rp8ikad649IgxNOJ8myyCUnVnvPL7zM1tcYiQVwXQ6kE-4zBoF8ms1WeMBprEaUOfketPJBMbA5eas9K9B37OU497_NmMIZgRixgm9Wh1iO6J69p72CC0j5subgG_DJ9T3CvjyLnHikD45ybser02RPh8h84-NdDR5CxAAAAAUGEvugA")
BOT_TOKEN = getenv("BOT_TOKEN", "5538104001:AAFVyMP2aBCS_uvqg8QovKAQlb8D_ac0rrk")
BOT_NAME = getenv("BOT_NAME", "FeNix")
API_ID = int(getenv("API_ID", "16228886"))
API_HASH = getenv("API_HASH", "b7de6ba01d7af6fc2d99375b5fbd0f82")
OWNER_NAME = getenv("OWNER_NAME", "akeen")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ipiiii")
ALIVE_NAME = getenv("ALIVE_NAME", "akeen")
BOT_USERNAME = getenv("BOT_USERNAME", "ssTss_bot")
OWNER_ID = getenv("OWNER_ID", "5186954055")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "eNix_TeAm")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Mus_3b2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "iPiiii")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5186954055").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/1d5b44ab1e2ec79875ee1.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/fa9654c0e092f475d08fa.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Akeen-T/uiii")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/fa9654c0e092f475d08fa.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/76a5f7db1592ef41b6243.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/67c6d43a8372adf70bee5.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/26367707c59de5702a018.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/09f47e7be9f1d6fd7a5d2.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/2045f32756eadbadc7904.jpg")
