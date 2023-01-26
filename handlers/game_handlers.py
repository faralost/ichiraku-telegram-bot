from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from database.database import GAME_USERS, update_game_users_db
from lexicon.lexicon_ru import LEXICON_RU
from services.game_services import (
    get_stat_text,
    sort_by_win_rate,
    get_stats_text,
    cancel_the_game,
    enter_the_game,
    set_random_number_for_user,
    set_user_attempts,
    process_the_game,
)


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
        await message.reply(LEXICON_RU['not_registered_for_game'])
    else:
        await message.reply(text=get_stat_text(message.from_user.id))


async def process_stats_command(message: Message):
    sorted_by_win_rate = sort_by_win_rate(GAME_USERS)
    await message.reply(text=get_stats_text(sorted_by_win_rate))


async def process_cancel_command(message: Message):
    if message.from_user.id not in GAME_USERS:
        await message.reply(text=LEXICON_RU['not_registered_for_game'])
    else:
        if GAME_USERS[message.from_user.id]['in_game']:
            await message.reply(text=LEXICON_RU['canceled_game'])
            cancel_the_game(message.from_user.id)
        else:
            await message.answer(text=LEXICON_RU['not_playing'])


async def process_enter_command(message: Message):
    if message.from_user.id not in GAME_USERS:
        await message.reply(text=LEXICON_RU['not_registered_for_game'])
    else:
        if not GAME_USERS[message.from_user.id]['in_game']:
            await message.reply(text=LEXICON_RU['new_game'])
            enter_the_game(message.from_user.id)
            set_random_number_for_user(message.from_user.id)
            set_user_attempts(message.from_user.id)
        else:
            await message.reply(text=LEXICON_RU['we_are_playing'])


async def process_numbers_command(message: Message):
    if message.from_user.id not in GAME_USERS:
        await message.reply(text=LEXICON_RU['not_registered_for_game'])
    else:
        if GAME_USERS[message.from_user.id]['in_game']:
            await process_the_game(message)
        else:
            await message.reply(text=LEXICON_RU['not_playing'])
        update_game_users_db(GAME_USERS)


def register_game_handlers(dp: Dispatcher):
    dp.register_message_handler(process_game_command, commands='game')
    dp.register_message_handler(process_stat_command, commands='stat')
    dp.register_message_handler(process_stats_command, commands='stats')
    dp.register_message_handler(process_cancel_command, commands='cancel')
    dp.register_message_handler(process_enter_command, Text(equals=['Давай', 'Игра', 'Го'], ignore_case=True))
    dp.register_message_handler(
        process_numbers_command,
        lambda message: message.text.isdigit() and 1 <= int(message.text) <= 100
    )
