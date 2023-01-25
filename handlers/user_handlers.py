from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU


async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
