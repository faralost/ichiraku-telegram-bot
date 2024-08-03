import asyncio
import datetime

import aioschedule
from aiogram import Bot
from pytz import timezone

from config_data.config import ICHIRAKU_CHAT_ID
from database.database import ALL_CHATS, BIRTHDAYS

from external_services.api_ninjas import collect_fact
from external_services.fx import collect_currencies
from external_services.openweather import collect_weather
from external_services.animechan import collect_quote, get_random_anime, TOP_ANIMES
from keyboards.keyboards import fact_keyboard, quote_keyboard, weather_keyboard
from lexicon.helpers import get_birthday_text, get_apple_music_notification_text, get_bot_birthday_text
from lexicon.lexicon_ru import LEXICON_RU
from services.services import send_to_all_chats

FIRST_DAY_OF_MONTH = 1


async def send_good_morning(bot: Bot):
    text = LEXICON_RU['good_morning'] + LEXICON_RU['todays_weather']
    text += await collect_weather()
    text += LEXICON_RU['currencies'] + await collect_currencies()
    await send_to_all_chats(ALL_CHATS, bot, text, reply_markup=weather_keyboard)


async def send_anime_quote(bot: Bot):
    text = LEXICON_RU['quote_of_the_day'] + await collect_quote(get_random_anime(TOP_ANIMES))
    await send_to_all_chats(ALL_CHATS, bot, text, reply_markup=quote_keyboard)


async def send_fact(bot: Bot):
    text = LEXICON_RU['fact_of_the_day'] + await collect_fact()
    await send_to_all_chats(ALL_CHATS, bot, text, reply_markup=fact_keyboard)


async def check_birthdays(bot: Bot):
    today = datetime.datetime.now(timezone('Asia/Bishkek'))
    today_str = today.strftime('%d-%m')
    if today_str in BIRTHDAYS:
        text = await get_birthday_text(today_str)
        await bot.send_message(ICHIRAKU_CHAT_ID, text)


async def send_bot_birthday(bot: Bot):
    today = datetime.datetime.now(timezone('Asia/Bishkek'))
    today_str = today.strftime('%d-%m')
    if today_str == '30-12':
        years_old = datetime.datetime.now().year - datetime.datetime(2022, 12, 30).year
        text = await get_bot_birthday_text(years_old)
        await bot.send_photo(
            ICHIRAKU_CHAT_ID,
            'https://ik.imagekit.io/faralost/bot_birthday.jpg'
        )
        await bot.send_message(ICHIRAKU_CHAT_ID, text)


async def check_apple_music_notification(bot: Bot):
    today = datetime.datetime.now(timezone('Asia/Bishkek'))
    month_name = today.strftime("%B")
    if today.day == FIRST_DAY_OF_MONTH:
        text = await get_apple_music_notification_text(month_name)
        await bot.send_message(ICHIRAKU_CHAT_ID, text)


async def scheduler(bot: Bot):
    aioschedule.every().day.at('02:00').do(send_good_morning, bot)
    aioschedule.every().day.at('06:00').do(send_anime_quote, bot)
    aioschedule.every().day.at('12:00').do(send_fact, bot)
    aioschedule.every().day.at('18:01').do(check_birthdays, bot)
    aioschedule.every().day.at('03:00').do(check_apple_music_notification, bot)
    aioschedule.every().day.at('04:00').do(send_bot_birthday, bot)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
