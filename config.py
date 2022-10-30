## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQC4sGYAh3emE-gnr2dFULcWrtecrdNriWi2SoLkup6HemQhc5Z-waNCtukHYVSZor1cDTrYyq1pu81MKHRV0_VvRUNDuyyqeqpdh0BNigiwnc08zzd3XO8ZCMCzE_yt2mu6FxDDn1x-pUHvtbgdSeYVecXEt-wEgBAsgPbVvstO9zSVqtK8s8U_8KichwuOPX9r1GIlpEheu_ZWlt0PpcuRHz3xde6aQk5aCuDvgsbXqy_0fzdOdiWUDokP_Uh_29sOTpfCXEtC_o5c-phfn0crtYjZOtv3zZBNUrwgomp7Hj8_EyrlJLpQTFTrfThfc_KNJKr6bPgU_XdINV1Q_gGNby8t-gAAAAFU_2aVAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5638976866:AAHfN7aRo1-9AUkaqQ8suauN33YcD2HkWV8")
BOT_NAME = getenv("BOT_NAME", "FeNix")
API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
OWNER_NAME = getenv("OWNER_NAME", "Akeen")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ipiiii")
ALIVE_NAME = getenv("ALIVE_NAME", "Akeen")
BOT_USERNAME = getenv("BOT_USERNAME", "MusicTxnBot")
OWNER_ID = getenv("OWNER_ID", "5186954055")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Gooo2bot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FIINJAKE")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Mus_3b2")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "iPiiii")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5186954055").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/318172684145488402edb.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/49b677c39b29994da0c68.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RR8R9-muntazer/btk")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/39c6305b5de327544264a.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/b96757b04e6aeb6e5e069.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/6dbc099e85a19017bfd20.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/790c4f0dc937b1844f2d1.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/020948e6aeb7467771ef0.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/8cd16c476ff66c580a3ce.jpg")
