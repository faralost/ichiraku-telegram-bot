import httpx
from unittest.mock import patch, AsyncMock
import pytest

from config_data import config
from errors.errors import NinjasAPIError
from external_services.api_ninjas import get_fact

ninjas_fact_response = [{'fact': 'fact'}]


@pytest.mark.asyncio
async def test_get_fact():
    with patch('httpx.AsyncClient.get', AsyncMock(return_value=httpx.Response(200, json=ninjas_fact_response))) as m:
        response = await get_fact()
        assert response == 'fact'
        m.assert_called_once_with(
            'https://api.api-ninjas.com/v1/facts?limit=1', headers={'X-Api-Key': config.API_NINJAS_KEY}
        )

    with patch('httpx.AsyncClient.get', AsyncMock(side_effect=httpx.RequestError('Error'))):
        with pytest.raises(NinjasAPIError):
            await get_fact()
