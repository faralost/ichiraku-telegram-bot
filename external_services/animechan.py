import logging
import random
from dataclasses import dataclass

import httpx
from mtranslate import translate

from errors.error_messages import ERROR_MESSAGES_RU
from errors.errors import AnimechanAPIError
from lexicon.lexicon_ru import LEXICON_RU

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


async def get_anime_quote(anime_title: str) -> dict[str, str]:
    url = f'https://animechan.xyz/api/random/anime?title={anime_title}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == httpx.codes.OK:
                return response.json()
            raise AnimechanAPIError
        except httpx.RequestError as e:
            logging.error(e)
            raise AnimechanAPIError


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
    text = f'{LEXICON_RU["anime"]}: {quote.anime}\n'
    text += f'{LEXICON_RU["character"]}: <b>{quote.character} ©</b>\n\n'
    text += f'- <b>"{quote.quote}"</b>'
    return text


def get_random_anime(animes: tuple[str, ...]):
    return random.choice(animes)
