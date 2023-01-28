import logging

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.exceptions import Unauthorized, BadRequest

from database.database import update_all_chats_db, BIRTHDAYS
from lexicon.lexicon_ru import LEXICON_RU


async def send_to_all_chats(chats: set[int], bot: Bot, text: str, reply_markup: InlineKeyboardMarkup = None):
    for chat_id in chats.copy():
        try:
            await bot.send_message(chat_id, text, reply_markup=reply_markup)
        except (Unauthorized, BadRequest) as e:
            logging.error(e)
            chats.remove(chat_id)
            update_all_chats_db(chats)


async def get_birthday_text(birthday: str) -> str:
    return LEXICON_RU['birthday_text'] + f'<tg-spoiler><b>{BIRTHDAYS[birthday]}</b></tg-spoiler>'
