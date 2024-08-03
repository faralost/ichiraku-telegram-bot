import logging
from dataclasses import dataclass

import httpx

from config_data import config
from errors.error_messages import ERROR_MESSAGES_RU
from errors.errors import FxAPIError
from lexicon.lexicon_ru import LEXICON_RU


@dataclass
class CurrencySom:
    usd_buy: str
    usd_sell: str
    eur_buy: str
    eur_sell: str
    tenge_buy: str
    tenge_sell: str


async def get_currencies() -> str:
    url = 'https://data.fx.kg/api/v1/current'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers={'Authorization': f"Bearer {config.FX_API_KEY}"})
            if response.status_code == httpx.codes.OK:
                return response.json()[1]
            raise FxAPIError
        except httpx.RequestError as e:
            logging.error(e)
            raise FxAPIError


async def parse_currencies(currencies: dict) -> CurrencySom:
    try:
        return CurrencySom(
            usd_buy=currencies['rates'][1]["buy_usd"],
            usd_sell=currencies['rates'][1]["sell_usd"],
            eur_buy=currencies['rates'][1]["buy_eur"],
            eur_sell=currencies['rates'][1]["sell_eur"],
            tenge_buy=currencies['rates'][1]["buy_kzt"],
            tenge_sell=currencies['rates'][1]["sell_kzt"],
        )
    except KeyError:
        raise FxAPIError

async def collect_currencies():
    try:
        currencies_response = await get_currencies()
        currencies = await parse_currencies(currencies_response)
        return get_currencies_text(currencies)
    except FxAPIError:
        return ERROR_MESSAGES_RU['currencies_error']


def get_currencies_text(currencies: CurrencySom) -> str:
    text = (f'<b>Покупка</b>:\n'
            f'USD: {currencies.usd_buy}, EUR: {currencies.eur_buy}, KZT: {currencies.tenge_buy}\n\n'
            f'<b>Продажа</b>:\n'
            f'USD: {currencies.usd_sell}, EUR: {currencies.eur_sell}, KZT: {currencies.tenge_sell}')
    return text
