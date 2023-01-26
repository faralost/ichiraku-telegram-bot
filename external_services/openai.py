import logging

import openai
from openai import OpenAIError

from config_data import config
from errors.error_messages import ERROR_MESSAGES_RU

openai.api_key = config.OPENAI_API_KEY


def get_openai_response(text):
    try:
        return openai.Completion.create(
            engine='text-davinci-003',
            prompt=f'{text}',
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
    except OpenAIError as e:
        logging.error(e)
        return ERROR_MESSAGES_RU['openai_error']
