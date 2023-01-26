from database.database import GAME_USERS

ATTEMPTS = 5


def get_user_total_games(user_id: int) -> int:
    return GAME_USERS[user_id]["total_games"]


def get_user_total_wins(user_id: int) -> int:
    return GAME_USERS[user_id]["wins"]


def get_user_total_losses(user_id: int) -> int:
    return GAME_USERS[user_id]["losses"]


def get_user_username(user_id: int) -> str:
    return f'@{GAME_USERS[user_id]["username"]}'


def get_stat_text(user_id: int) -> str:
    from lexicon.lexicon_ru import LEXICON_RU
    return f"{LEXICON_RU['stat']}\n\n" \
           f"{LEXICON_RU['player']}: {get_user_username(user_id)}\n" \
           f"{LEXICON_RU['games_played']}: <b>{get_user_total_games(user_id)}</b>\n" \
           f"{LEXICON_RU['game_wins']}: <b>{get_user_total_wins(user_id)}</b>\n" \
           f"{LEXICON_RU['game_losses']}: <b>{get_user_total_losses(user_id)}</b>\n"
