from unittest.mock import patch, AsyncMock

import httpx
import pytest

from config_data import config
from errors.errors import OpenWeatherAPIError
from external_services.openweather import get_openweather

openweather_response = {
    'timezone': 'Asia/Bishkek',
    'daily': [
        {
            'temp': {
                'min': -5,
                'max': 10
            },
            'weather': [
                {
                    'description': 'light snow',
                    'id': 600
                }
            ]
        }
    ]
}

params = {
    'appid': config.OPEN_WEATHER_KEY,
    'lang': 'ru',
    'units': 'metric',
    'cnt': 2,
    'exclude': 'minutely,hourly,alerts'
}


@pytest.mark.asyncio
async def test_get_openweather():
    lat = 12.2
    lon = 13.3
    with patch('httpx.AsyncClient.get', AsyncMock(return_value=httpx.Response(200, json=openweather_response))) as m:
        response = await get_openweather(lat=lat, lon=lon)
        assert response == openweather_response
        m.assert_called_once_with(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}', params=params)

    with patch('httpx.AsyncClient.get', AsyncMock(side_effect=httpx.RequestError('Error'))):
        with pytest.raises(OpenWeatherAPIError):
            await get_openweather(lat=lat, lon=lon)
