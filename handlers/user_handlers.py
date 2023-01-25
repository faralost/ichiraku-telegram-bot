from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU
from services.fact_services import collect_fact


async def process_start_command(message: Message):
    await message.reply(text=LEXICON_RU['start'])


async def process_help_command(message: Message):
    await message.reply(text=LEXICON_RU['help'])


async def process_fact_command(message: Message):
    await message.answer_chat_action('typing')
    fact = await collect_fact()
    await message.reply(text=fact)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_fact_command, commands='fact')
