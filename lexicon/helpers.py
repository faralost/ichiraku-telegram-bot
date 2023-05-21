from database.database import BIRTHDAYS
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_RU_MONTHS


async def get_birthday_text(birthday: str) -> str:
    return LEXICON_RU['birthday_text'] + f'<tg-spoiler><b>{BIRTHDAYS[birthday]}</b></tg-spoiler>'


async def get_apple_music_notification_text(month_name: str) -> str:
    return LEXICON_RU['apple_music_notification_text'] + f'<b>{LEXICON_RU_MONTHS[month_name]}</b>'
