import logging
import math
from dataclasses import dataclass

import httpx

from config_data import config
from errors.error_messages import ERROR_MESSAGES_RU
from errors.errors import OpenWeatherAPIError
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_RU_CITIES

CITIES = {
    'tokmok': {'lat': 42.84194, 'lon': 75.30149},
    'bishkek': {'lat': 42.882004, 'lon': 74.582748},
    'almaty': {'lat': 43.238949, 'lon': 76.889709},
}

WEATHER_ID_EMOJIS = {
    801: '🌤',
    802: '⛅️',
    803: '🌥',
    804: '☁️',
    800: '☀️',
    200: '⛈',
    201: '⛈',
    202: '⛈',
    210: '⛈',
    211: '⛈',
    212: '⛈',
    221: '⛈',
    230: '⛈',
    231: '⛈',
    232: '⛈',
    300: '🌨',
    301: '🌨',
    302: '🌨',
    310: '🌨',
    311: '🌨',
    312: '🌨',
    313: '🌨',
    314: '🌨',
    321: '🌨',
    500: '🌧',
    501: '🌧',
    502: '☔️',
    503: '☔️',
    504: '☔️',
    511: '❄️',
    520: '☔️',
    521: '☔️',
    522: '☔️',
    531: '☔️',
    600: '❄️',
    601: '❄️',
    602: '❄️',
    611: '❄️',
    612: '❄️',
    613: '❄️',
    615: '❄️',
    616: '❄️',
    620: '❄️',
    621: '❄️',
    622: '❄️',
    701: '🌫',
    711: '🌫',
    721: '🌫',
    731: '🌬',
    741: '🌫',
    751: '🌬',
    761: '🌬',
    762: '🌋',
    771: '🌬',
    781: '🌪'
}


@dataclass
class OpenWeather:
    timezone: str
    lat: float
    lon: float
    min_temp: int
    max_temp: int
    description: str
    weather_id: int


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


async def parse_openweather(openweather: dict) -> OpenWeather:
    return OpenWeather(
        timezone=openweather['timezone'],
        lat=openweather['lat'],
        lon=openweather['lon'],
        min_temp=math.ceil(openweather['daily'][0]['temp']['min']),
        max_temp=math.ceil(openweather['daily'][0]['temp']['max']),
        description=openweather['daily'][0]['weather'][0]['description'],
        weather_id=openweather['daily'][0]['weather'][0]['id']
    )


async def get_weather_text(lat: float, lon: float) -> str:
    openweather_response = await get_openweather(lat=lat, lon=lon)
    parsed_weather = await parse_openweather(openweather_response)
    text = f'<b>{LEXICON_RU_CITIES[str(parsed_weather.lon)]}</b>\n' \
           f'{LEXICON_RU["min_temp"]}: {parsed_weather.min_temp}°, ' \
           f'{LEXICON_RU["max_temp"]}: {parsed_weather.max_temp}°, ' \
           f'{parsed_weather.description}{WEATHER_ID_EMOJIS[parsed_weather.weather_id]}\n\n'
    return text


async def collect_weather() -> str:
    try:
        collected_weather = ''
        for city in CITIES:
            weather = await get_weather_text(lat=CITIES[city]['lat'], lon=CITIES[city]['lon'])
            collected_weather += weather
        return collected_weather
    except OpenWeatherAPIError:
        return ERROR_MESSAGES_RU['weather_error']
