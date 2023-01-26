from aiogram import Dispatcher
from aiogram.types import Message

from database.database import GAME_USERS
from lexicon.lexicon_ru import LEXICON_RU
from services.game_services import get_stat_text


async def process_game_command(message: Message):
    if message.from_user.id not in GAME_USERS:
        GAME_USERS[message.from_user.id] = {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0,
            'losses': 0,
            'username': message.from_user.username,
            'win_rate': 0
        }
    await message.reply(text=LEXICON_RU['game'])


async def process_stat_command(message: Message):
    if message.from_user.id not in GAME_USERS:
        await message.reply(LEXICON_RU['not_in_game'])
    else:
        await message.reply(text=get_stat_text(message.from_user.id))


def register_game_handlers(dp: Dispatcher):
    dp.register_message_handler(process_game_command, commands='game')
    dp.register_message_handler(process_stat_command, commands='stat')
