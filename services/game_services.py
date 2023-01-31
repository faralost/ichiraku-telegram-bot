from database.database import GAME_USERS
from utils.utils import get_random_number

ATTEMPTS = 5


def get_user_total_games(user_id: int) -> int:
    return GAME_USERS[user_id]["total_games"]


def get_user_total_wins(user_id: int) -> int:
    return GAME_USERS[user_id]["wins"]


def get_user_total_losses(user_id: int) -> int:
    return GAME_USERS[user_id]["losses"]


def get_user_username(user_id: int) -> str:
    return f'@{GAME_USERS[user_id]["username"]}'


def cancel_the_game(user_id: int) -> None:
    GAME_USERS[user_id]['in_game'] = False


def enter_the_game(user_id: int) -> None:
    GAME_USERS[user_id]['in_game'] = True


def set_random_number_for_user(user_id: int) -> None:
    GAME_USERS[user_id]['secret_number'] = get_random_number(100)


def get_random_number_of_user(user_id: int) -> str:
    return f"{GAME_USERS[user_id]['secret_number']}"


def set_user_attempts(user_id: int) -> None:
    GAME_USERS[user_id]['attempts'] = ATTEMPTS


def get_user_attempts(user_id: int) -> str:
    return f'{GAME_USERS[user_id]["attempts"]}'


def decrement_attempts(user_id: int) -> None:
    GAME_USERS[user_id]['attempts'] -= 1


def increment_total_games(user_id: int) -> None:
    GAME_USERS[user_id]['total_games'] += 1


def increment_wins(user_id: int) -> None:
    GAME_USERS[user_id]['wins'] += 1


def increment_losses(user_id: int) -> None:
    GAME_USERS[user_id]['losses'] += 1


def recalculate_win_rate(user_id: int) -> None:
    GAME_USERS[user_id]['win_rate'] = (GAME_USERS[user_id]['wins'] / GAME_USERS[user_id]['total_games'] * 100)


def get_stat_text(user_id: int) -> str:
    from lexicon.lexicon_ru import LEXICON_RU
    return f"{LEXICON_RU['stat']}\n\n" \
           f"{LEXICON_RU['player']}: {get_user_username(user_id)}\n" \
           f"{LEXICON_RU['games_played']}: <b>{get_user_total_games(user_id)}</b>\n" \
           f"{LEXICON_RU['game_wins']}: <b>{get_user_total_wins(user_id)}</b>\n" \
           f"{LEXICON_RU['game_losses']}: <b>{get_user_total_losses(user_id)}</b>\n"


def sort_by_win_rate(game_users: dict) -> list:
    return sorted(game_users.values(), key=lambda x: x['win_rate'], reverse=True)


def get_stats_text(sorted_users: list) -> str:
    from lexicon.lexicon_ru import LEXICON_RU
    stats = f"{LEXICON_RU['stats']}\n\n"
    for i in range(len(sorted_users)):
        stats += f'{i + 1} @{sorted_users[i]["username"]} побед: {round(sorted_users[i]["win_rate"])}%\n'
    return stats


async def process_the_game(message):
    from lexicon.lexicon_ru import LEXICON_RU
    if int(message.text) == GAME_USERS[message.from_user.id]['secret_number']:
        await message.reply(text=LEXICON_RU['won_the_game'])
        cancel_the_game(message.from_user.id)
        increment_total_games(message.from_user.id)
        increment_wins(message.from_user.id)
        recalculate_win_rate(message.from_user.id)
    elif int(message.text) > GAME_USERS[message.from_user.id]['secret_number']:
        decrement_attempts(message.from_user.id)
        await message.reply(text=LEXICON_RU['number_is_smaller'] + get_user_attempts(message.from_user.id))
    elif int(message.text) < GAME_USERS[message.from_user.id]['secret_number']:
        decrement_attempts(message.from_user.id)
        await message.reply(text=LEXICON_RU['number_is_bigger'] + get_user_attempts(message.from_user.id))
    if GAME_USERS[message.from_user.id]['attempts'] == 0:
        await message.reply(text=LEXICON_RU['lose_the_game'] + get_random_number_of_user(message.from_user.id))
        cancel_the_game(message.from_user.id)
        increment_losses(message.from_user.id)
        increment_total_games(message.from_user.id)
        recalculate_win_rate(message.from_user.id)
