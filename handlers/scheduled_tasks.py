import asyncio
import datetime

import aioschedule
from aiogram import Bot
from pytz import timezone

from config_data.config import ICHIRAKU_CHAT_ID
from database.database import ALL_CHATS, BIRTHDAYS
from keyboards.keyboards import fact_keyboard, quote_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from services.anime_quote_services import collect_quote, TOP_ANIMES, get_random_anime
from services.fact_services import collect_fact
from services.openweather_services import collect_weather
from services.services import send_to_all_chats, get_birthday_text


async def send_good_morning(bot: Bot):
    text = LEXICON_RU['good_morning'] + LEXICON_RU['todays_weather']
    text += await collect_weather()
    await send_to_all_chats(ALL_CHATS, bot, text)


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


async def scheduler(bot: Bot):
    aioschedule.every().day.at('02:00').do(send_good_morning, bot)
    aioschedule.every().day.at('06:00').do(send_anime_quote, bot)
    aioschedule.every().day.at('12:00').do(send_fact, bot)
    aioschedule.every().day.at('18:01').do(check_birthdays, bot)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
