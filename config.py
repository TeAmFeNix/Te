## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BACWqN3vI_UtQgu2u2V2LS84jUQkvytPVlo9emT2NswUQUriR7QVXDyu0fCVRwlNAVZhDu7Ac2Xq_roBdajCTDRWS1U-AsUovwXM_t9GJfWxT0FVERTj3V5kEjm2966RWY4SUpAOYL03homASerWJetgGC-fLqZsV6O6LoO66MZISoQNKtDvrFSp3LlVF0Teuq1i0B1yDr2RhUzT21zzDsg2_k-aRacZ9fBpJKsozXrm7Yc91MxE81XBf1izZbCaZYa0yFV2_-9TfjGPukJx2dkOJ6U6ccvFoWM5wG6IEao5ibxlRcORBODNCGbIhnGgXl1hl0hEh3fhgH3fXQag2XPcAAAAAVIOe08A")
BOT_TOKEN = getenv("BOT_TOKEN", "5538104001:AAFZmQvf1PdnL9JASsdxu0y11E09vytI2Qk")
BOT_NAME = getenv("BOT_NAME", "FeNix")
API_ID = int(getenv("API_ID", "15041781"))
API_HASH = getenv("API_HASH", "7bab59794fa1fa47d165bbf6eee6b8be")
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
