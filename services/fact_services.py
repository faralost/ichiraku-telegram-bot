from mtranslate import translate

from errors.error_messages import ERROR_MESSAGES_RU
from errors.errors import NinjasAPIError
from external_services.api_ninjas_fact import get_fact


async def collect_fact():
    try:
        fact = await get_fact()
        translation = translate(fact, 'ru', 'en')
        if translation:
            return '\n\n'.join([f'<b>{fact}</b>', f'<i>{translation}</i>'])
        return f'<b>{fact}</b>'
    except NinjasAPIError:
        return ERROR_MESSAGES_RU['fact_error']


