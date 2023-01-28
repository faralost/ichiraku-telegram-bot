import httpx
import pytest
from unittest.mock import AsyncMock, patch

from errors.errors import AnimechanAPIError
from external_services.animechan import get_anime_quote

anime_quote_response = {
    'anime': 'Naruto',
    'character': 'Naruto Uzumaki',
    'quote': 'I will never go back on my word, that is my ninja way!'
}


@pytest.mark.asyncio
async def test_get_anime_quote():
    with patch('httpx.AsyncClient.get', AsyncMock(return_value=httpx.Response(200, json=anime_quote_response))) as m:
        response = await get_anime_quote('Naruto')
        assert response == anime_quote_response
        m.assert_called_once_with('https://animechan.vercel.app/api/random/anime?title=Naruto')

    with patch('httpx.AsyncClient.get', AsyncMock(side_effect=httpx.RequestError('Error'))):
        with pytest.raises(AnimechanAPIError):
            await get_anime_quote('Naruto')
