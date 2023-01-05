import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class TelegramBot:
    token: str


@dataclass
class ExternalService:
    open_weather_token: str
    api_ninjas_token: str


@dataclass
class Config:
    telegram_bot: TelegramBot
    external_service: ExternalService


config = Config(
    telegram_bot=TelegramBot(token=os.getenv('BOT_API_TOKEN')),
    external_service=ExternalService(open_weather_token=os.getenv('OPEN_WEATHER_KEY'),
                                     api_ninjas_token=os.getenv('API_NINJAS_KEY'))
)
