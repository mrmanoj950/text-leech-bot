import os

API_ID    = os.environ.get("API_ID", "23069582")
API_HASH  = os.environ.get("API_HASH", "b3b56eaf67828684f54d540f684fdf1f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7672004632:AAHohyBfssnv2Nlscz0tqiji3r1I7pfsdUc") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
