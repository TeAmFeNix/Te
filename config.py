## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBMHnr60MEBJ3RboF8KIT8fMH7P-LZklxAfasxo8HaT_Me45CqEfdiv0iXfF0Iss1p49ccjO-yXyFDsp8gvayJowr-SaIehnAr-jeLSOsi2LvqeqnsC1bConEt8tscogd1kp51qS2Xq7NTHSnuE9F7gqvtuKKG8p2KtEJRNVpBQLN-snbmoDgDsobkVs54PnRDC3Weu1TL969tAG6bQSTC6KgJ2Gstu0E5yPMZdyWmtvz19lXj7PN5aKwRr41V0mcKKSPyswsUAUAzt8GgvnPnvoF0ewh1DrkUKuYy-oEKcaNq_DvSFGV5D14u8PlmJk24sijpQfqH03ggmjkGhD8nzAAAAAUuthdYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5436614046:AAExhX6fZEBjW_eTEkEi5z0roCLAZ0Sl34g")
BOT_NAME = getenv("BOT_NAME", "m")
API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
OWNER_NAME = getenv("OWNER_NAME", "mm")
OWNER_USERNAME = getenv("OWNER_USERNAME", "urrrrc")
ALIVE_NAME = getenv("ALIVE_NAME", "mm")
BOT_USERNAME = getenv("BOT_USERNAME", "eixibot")
OWNER_ID = getenv("OWNER_ID", "1254750804")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kind")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FIINJAKE")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "rlllrl")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5413098804").split()))
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
