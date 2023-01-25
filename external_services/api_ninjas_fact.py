import logging

import httpx

from config_data import config
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
