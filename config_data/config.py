import os
from dotenv import load_dotenv

load_dotenv()

BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')
OPEN_WEATHER_KEY = os.getenv('OPEN_WEATHER_KEY')
API_NINJAS_KEY = os.getenv('API_NINJAS_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
