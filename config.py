## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBbyKQF62Aq9ZIrQZRIcbAUuPaYCfy19qZmWVaSN7KHEuPdPCG5nwxtLnRYH3UU9KHZewvjdvoyfgTe6FYKeZE3W8cwaAGS-zu_BlA0P7LI81TMa2a5Kn7nDsKXmx1l18hBIw-BD-crB-9GfrJ-cmHCBeLUAk38HDeM2PPLKS7IE8CqAaW1X1vj29yLdfkbkvOTOe9n7HudVsGe4SiTFZqjWxVAZtlt2s9uOoZlCOop_uqsndW-1YSSgniI88zH88KkTQ2oPoZb5vgrSZc_xArJDlp0dnRQvGuxHNB94L7WiVdSWiVdp9IqK39R7skl1OE9c6Z0QLWO4qogjzXz9iSLAAAAAVRi_IAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5719110483:AAGaUDt9Ryp8-xTNPzHa-LuQ9rDbsIF9oXA")
BOT_NAME = getenv("BOT_NAME", "FeNix")
API_ID = int(getenv("API_ID", "15041781"))
API_HASH = getenv("API_HASH", "7bab59794fa1fa47d165bbf6eee6b8be")
OWNER_NAME = getenv("OWNER_NAME", "akeen")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ipiiii")
ALIVE_NAME = getenv("ALIVE_NAME", "akeen")
BOT_USERNAME = getenv("BOT_USERNAME", "Sgvxfgfbot")
OWNER_ID = getenv("OWNER_ID", "5186954055")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AkenkBot")
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
