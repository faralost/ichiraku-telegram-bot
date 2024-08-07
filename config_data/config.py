import os
from dotenv import load_dotenv

load_dotenv()

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')
API_NINJAS_KEY = os.environ['API_NINJAS_KEY']
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ICHIRAKU_CHAT_ID = os.getenv('ICHIRAKU_CHAT_ID')
WAIFU_API_KEY = os.getenv('WAIFU_API_KEY')
FX_API_KEY = os.getenv('FX_API_TOKEN')

IMAGEKIT_PRIVATE_KEY = os.getenv('IMAGEKIT_PRIVATE_KEY')
IMAGEKIT_PUBLIC_KEY = os.getenv('IMAGEKIT_PUBLIC_KEY')

SENTRY_DSN = os.getenv('SENTRY_DSN')

ADMIN_ID = os.getenv('ADMIN_ID')
