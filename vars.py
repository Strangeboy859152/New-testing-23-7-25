#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29223018"))
API_HASH = environ.get("API_HASH", "25b493c4989d22d7f2482f752d3d99ee")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "8167879352"))
CREDIT = environ.get("CREDIT", "【『 STRANGER BOYS 』】")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8167879352, 6039166844, 7818565931, 6126688051, 7568561381').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8167879352, 6039166844, 7818565931, 6126688051, 7568561381').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
