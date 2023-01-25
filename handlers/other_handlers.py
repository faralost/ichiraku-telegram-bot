from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU


async def send_reverse_answer(message: Message):
    await message.reply(message.text[::-1])


def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(send_reverse_answer)
