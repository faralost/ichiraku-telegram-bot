import logging

import httpx
from mtranslate import translate

from config_data import config
from errors.error_messages import ERROR_MESSAGES_RU
from errors.errors import WaifuAPIError
from external_services.animechan import AnimeQuote, get_quote_text


async def get_anime_quote() -> dict[str, str]:
    url = f'https://waifu.it/api/v4/quote'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers={"Authorization": config.WAIFU_API_KEY})
            if response.status_code == httpx.codes.OK:
                return response.json()
            raise WaifuAPIError
        except httpx.RequestError as e:
            logging.error(e)
            raise WaifuAPIError


async def parse_anime_quote(anime_quote: dict[str, str]) -> AnimeQuote:
    return AnimeQuote(
        anime=anime_quote['anime'],
        character=anime_quote['author'],
        quote=anime_quote['quote']
    )


async def collect_quote():
    try:
        quote_response = await get_anime_quote()
        quote = await parse_anime_quote(quote_response)
        translation = translate(quote.quote, 'ru', 'en')
        if translation:
            return '\n\n'.join([get_quote_text(quote), f'- <i>"{translation}"</i>'])
        return get_quote_text(quote)
    except WaifuAPIError:
        return ERROR_MESSAGES_RU['quote_error']
