from database.database import get_all_chats_users_count
from lexicon.lexicon_ru import LEXICON_RU


def collect_bot_stats_text() -> str:
    text = f"<b>{LEXICON_RU['admin_stats']}</b>\n\n"
    text += f'Кол-во активных пользователей: {get_all_chats_users_count()}'
    return text


def get_bot_stats() -> str:
    return collect_bot_stats_text()
