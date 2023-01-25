import logging

import httpx

from errors.errors import AnimechanAPIError


async def get_anime_quote(anime_title: str) -> dict[str, str]:
    url = f'https://animechan.vercel.app/api/random/anime?title={anime_title}'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == httpx.codes.OK:
                return response.json()
            raise AnimechanAPIError
        except httpx.RequestError as e:
            logging.error(e)
            raise AnimechanAPIError
