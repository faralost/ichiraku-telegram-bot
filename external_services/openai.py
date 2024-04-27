import logging

from openai import OpenAIError, OpenAI

from config_data import config
from errors.error_messages import ERROR_MESSAGES_RU

api_key = config.OPENAI_API_KEY

client = OpenAI(api_key=api_key)


def get_openai_response(text):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You as assistant help users with their questions.",
                },
                {"role": "user", "content": text},
            ],
            model='gpt-3.5-turbo'
        )
        return response['choices'][0].message.content
    except OpenAIError as e:
        logging.error(e)
        return ERROR_MESSAGES_RU['openai_error']
