from typing import TypedDict


class ErrorMessage(TypedDict):
    fact_error: str
    quote_error: str
    currencies_error: str
    weather_error: str
    openai_error: str


ERROR_MESSAGES_RU: ErrorMessage = {
    'fact_error': '<i>При получении факта произошла ошибка...</i>',
    'quote_error': '<i>При получении цитаты произошла ошибка...</i>',
    'currencies_error': '<i>При получении валют произошла ошибка...</i>',
    'weather_error': '<i>При получении погоды произошла ошибка...</i>',
    'openai_error': '<i>При получении ответа от chatGPT произошла ошибка...</i>',
}
