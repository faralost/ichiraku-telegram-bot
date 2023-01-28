import logging

import httpx
from mtranslate import translate

from config_data import config
from errors.error_messages import ERROR_MESSAGES_RU
from errors.errors import NinjasAPIError


async def get_fact() -> str:
    url = 'https://api.api-ninjas.com/v1/facts?limit=1'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers={'X-Api-Key': config.API_NINJAS_KEY})
            if response.status_code == httpx.codes.OK:
                return response.json()[0]['fact']
            raise NinjasAPIError
        except httpx.RequestError as e:
            logging.error(e)
            raise NinjasAPIError


async def collect_fact():
    try:
        fact = await get_fact()
        translation = translate(fact, 'ru', 'en')
        if translation:
            return '\n\n'.join([f'<b>{fact}</b>', f'<i>{translation}</i>'])
        return f'<b>{fact}</b>'
    except NinjasAPIError:
        return ERROR_MESSAGES_RU['fact_error']
