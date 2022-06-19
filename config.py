## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgC5XrH4MqeorBF9w2L0m3Jwtp-SjsZkVQ-tQouHCSsBriquI4BbI7SOGK6-HTVqudFi2TZtxlbqQrE-4HHcn0X_RywSh6YIacd4gWwv8DZiw4HHk5AdQBMRvfM37o0OC5Ifg5Zs2jx3aIgtHSp2GskDLxjdRjQH5cnmX_4pZKxC56CwqjsFF5WJWY_crd__IyQClsRiqMvvBOV_zMdH2_w3OoRhS43b91hb6KfHqiCeJ5jVtoO5k26zA2Q6JZnDS7hlwhKfhSfV0neUzBhe-7tJIlwLAmIBELwJUUoC7OuigniTewBsleoWQ_ivSpUIZDs7zIlIzXYTfMYUc-U0JT_9AAAAATZ-UtMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5539489267:AAF2MUDACU-t80FmoJKCZz_-Rc7_R3h8v1k")
BOT_NAME = getenv("BOT_NAME", "𝐌𝐔𝐒𝐈𝐂 𝐅𝐈𝐍 ♫")
API_ID = int(getenv("API_ID", "13301444"))
API_HASH = getenv("API_HASH", "274d9263b17a07c2ff17f878b249ead0")
OWNER_NAME = getenv("OWNER_NAME", "ࢪﺿـاۅي اެبن الـدورة")
OWNER_USERNAME = getenv("OWNER_USERNAME", "R4005")
ALIVE_NAME = getenv("ALIVE_NAME", "ࢪﺿـاۅي اެبن الـدورة")
BOT_USERNAME = getenv("BOT_USERNAME", "MUSICFIINBOT")
OWNER_ID = getenv("OWNER_ID", "1254750804")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝐌𝐔𝐒𝐈𝐂 𝐉𝐀𝐊𝐄 ♫")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FIINJAKE")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "x02x2")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "x02x2")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://c.top4top.io/p_2344qvohj1.jpg")
START_PIC = getenv("START_PIC", "https://c.top4top.io/p_2344qvohj1.jpg")
DURATION_LIMIT = int(getenv("DhttpsURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://c.top4top.io/p_2344qvohj1.jpg")
IMG_2 = getenv("IMG_2", "https://c.top4top.io/p_2344qvohj1.jpg")
IMG_3 = getenv("IMG_3", "https://c.top4top.io/p_2344qvohj1.jpg")
IMG_4 = getenv("IMG_4", "https://c.top4top.io/p_2344qvohj1.jpg")
IMG_5 = getenv("IMG_5", "https://c.top4top.io/p_2344qvohj1.jpg")
IMG_6 = getenv("IMG_6", "https://c.top4top.io/p_2344qvohj1.jpg")
