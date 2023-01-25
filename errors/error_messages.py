from typing import TypedDict


class ErrorMessage(TypedDict):
    fact_error: str
    quote_error: str


ERROR_MESSAGES_RU: ErrorMessage = {
    'fact_error': '<i>При получении факта произошла ошибка...</i>',
    'quote_error': '<i>При получении цитаты произошла ошибка...</i>',
}
