import asyncio
import logging
from pprint import pprint

import httpx

from config_data import config
from errors.errors import OpenWeatherAPIError


async def get_openweather(lat: float, lon: float):
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}'
    params = {
        'appid': config.OPEN_WEATHER_KEY,
        'lang': 'ru',
        'units': 'metric',
        'cnt': 2,
        'exclude': 'minutely,hourly,alerts'
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            if response.status_code == httpx.codes.OK:
                return response.json()
            raise OpenWeatherAPIError
        except httpx.RequestError as e:
            logging.error(e)
            raise OpenWeatherAPIError
