import math
from dataclasses import dataclass

from errors.error_messages import ERROR_MESSAGES_RU
from errors.errors import OpenWeatherAPIError
from external_services.openweather import get_openweather
from lexicon.lexicon_ru import LEXICON_RU

CITIES = {
    'bishkek': {'lat': 42.882004, 'lon': 74.582748},
    'almaty': {'lat': 43.238949, 'lon': 76.889709},
    'novosibirsk': {'lat': 55.018803, 'lon': 82.933952},
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
    min_temp: int
    max_temp: int
    description: str
    weather_id: int


async def parse_openweather(openweather: dict) -> OpenWeather:
    return OpenWeather(
        timezone=openweather['timezone'],
        min_temp=math.ceil(openweather['daily'][0]['temp']['min']),
        max_temp=math.ceil(openweather['daily'][0]['temp']['max']),
        description=openweather['daily'][0]['weather'][0]['description'],
        weather_id=openweather['daily'][0]['weather'][0]['id']
    )


async def get_weather_text(lat: float, lon: float):
    openweather_response = await get_openweather(lat=lat, lon=lon)
    parsed_weather = await parse_openweather(openweather_response)
    text = f'<b>{LEXICON_RU[parsed_weather.timezone]}</b>\n' \
           f'{LEXICON_RU["min_temp"]}:{parsed_weather.min_temp}°, ' \
           f'{LEXICON_RU["max_temp"]}: {parsed_weather.max_temp}°, ' \
           f'{parsed_weather.description}{WEATHER_ID_EMOJIS[parsed_weather.weather_id]}\n\n'
    return text


async def collect_weather():
    try:
        collected_weather = ''
        for city in CITIES:
            weather = await get_weather_text(lat=CITIES[city]['lat'], lon=CITIES[city]['lon'])
            collected_weather += weather
        return collected_weather
    except OpenWeatherAPIError:
        return ERROR_MESSAGES_RU['weather_error']
