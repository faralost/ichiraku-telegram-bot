from aiogram import Dispatcher
from aiogram.types import Message

from database.database import GAME_USERS
from lexicon.lexicon_ru import LEXICON_RU


async def send_reverse_answer(message: Message):
    if message.from_user.id not in GAME_USERS:
        await message.reply('\n'.join([message.text[::-1], LEXICON_RU['smile']]))
    else:
        if GAME_USERS[message.from_user.id]['in_game']:
            await message.reply(text=LEXICON_RU['we_are_playing'])
        else:
            await message.reply('\n'.join([message.text[::-1], LEXICON_RU['smile']]))


def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(send_reverse_answer)
