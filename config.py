## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABIoRr8Pfgw9Xb4tnxnHteaJhgL4qQI6rJyA5lccCEUbvTRNWzX4F0MRNCgyM3IYqobNTfzqAGjBT1_VSNyOwY2i1drihBQFu0JQMi2YGCIOQD6WRHTNqpgg-5-WyyBHL1cxkpCTakF3YjeVAz9l8puBqDQdB2blWzCMvNVz8CbFNOEh5ShzH7t5IxtvaHo0sU5XOpUDVFxTaldfMFP9-Pj3xfZLD_tluSrfu4Rz4Kgj66drl-SCjOPaD6AkzfwmNqWXoQls6TECF_OU0hgm1Q6FSTQ5B54R5_qAmswUMcvybTJl6Ht7N2_avcZDtarccGqnLHYA_6nOS-KAeas8k7rAAAAAVRSvr4A")
BOT_TOKEN = getenv("BOT_TOKEN", "5540293954:AAEwL7X-bEHvzLCIc1Y_Yd3S_QdHKoQxdFY")
BOT_NAME = getenv("BOT_NAME", "m")
API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
OWNER_NAME = getenv("OWNER_NAME", "mm")
OWNER_USERNAME = getenv("OWNER_USERNAME", "R4005")
ALIVE_NAME = getenv("ALIVE_NAME", "mm")
BOT_USERNAME = getenv("BOT_USERNAME", "M_Uu_Bot")
OWNER_ID = getenv("OWNER_ID", "1254750804")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kind")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FIINJAKE")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "rr8r9")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "lilElil_5")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1754933021").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RR8R9-muntazer/btk")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
