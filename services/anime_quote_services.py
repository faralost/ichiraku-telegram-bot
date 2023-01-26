import random
from dataclasses import dataclass

from mtranslate import translate

from errors.error_messages import ERROR_MESSAGES_RU
from errors.errors import AnimechanAPIError
from external_services.animechan_quote import get_anime_quote

TOP_ANIMES = (
    'naruto',
    'jujutsu',
    'attack',
    'slayer',
    'haikyu',
    'note',
    'hunter',
    'evangelion',
    'brotherhood',
    'jojo',
    'punch',
)


@dataclass
class AnimeQuote:
    anime: str
    character: str
    quote: str


async def parse_anime_quote(anime_quote: dict[str, str]) -> AnimeQuote:
    return AnimeQuote(
        anime=anime_quote['anime'],
        character=anime_quote['character'],
        quote=anime_quote['quote']
    )


async def collect_quote(anime_title: str):
    try:
        quote_response = await get_anime_quote(anime_title)
        quote = await parse_anime_quote(quote_response)
        translation = translate(quote.quote, 'ru', 'en')
        if translation:
            return '\n\n'.join([get_quote_text(quote), f'- <i>"{translation}"</i>'])
        return get_quote_text(quote)
    except AnimechanAPIError:
        return ERROR_MESSAGES_RU['quote_error']


def get_quote_text(quote: AnimeQuote) -> str:
    text = f'Anime: <b>{quote.anime}</b>\n'
    text += f'Character: <b>{quote.character} ©</b>\n\n'
    text += f'- <b>"{quote.quote}"</b>'
    return text


def get_random_anime(animes: tuple[str]):
    return random.choice(animes)
