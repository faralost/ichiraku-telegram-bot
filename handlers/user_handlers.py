import openai
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from database.database import ALL_CHATS, add_chat_to_all_chats_db, update_all_chats_db
from external_services.animechan import collect_quote, get_random_anime, TOP_ANIMES
from external_services.api_ninjas import collect_fact
from external_services.openai import get_openai_response
from keyboards.keyboards import fact_keyboard, quote_keyboard
from lexicon.lexicon_ru import LEXICON_RU


async def process_start_command(message: Message):
    await message.reply(text=LEXICON_RU['start'])
    add_chat_to_all_chats_db(message.chat.id)
    update_all_chats_db(ALL_CHATS)


async def process_help_command(message: Message):
    await message.reply(text=LEXICON_RU['help'])


async def process_fact_command(message: Message):
    await message.answer_chat_action('typing')
    fact = await collect_fact()
    await message.reply(text=fact, reply_markup=fact_keyboard)


async def process_more_fact_press(callback: CallbackQuery):
    await callback.answer()
    fact = await collect_fact()
    await callback.message.reply(text=fact, reply_markup=fact_keyboard)


async def process_quote_command(message: Message):
    await message.answer_chat_action('typing')
    quote = await collect_quote(get_random_anime(TOP_ANIMES))
    await message.reply(text=quote, reply_markup=quote_keyboard)


async def process_more_quote_press(callback: CallbackQuery):
    await callback.answer()
    quote = await collect_quote(get_random_anime(TOP_ANIMES))
    await callback.message.reply(text=quote, reply_markup=quote_keyboard)


async def process_chat_gpt_command(message: Message):
    await message.answer_chat_action('typing')
    text = message.text.split(' ', 1)[1]
    response = get_openai_response(text)
    await message.reply(response.choices[0].text)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_fact_command, commands='fact')
    dp.register_callback_query_handler(process_more_fact_press, text='more_fact')
    dp.register_message_handler(process_quote_command, commands='quote')
    dp.register_callback_query_handler(process_more_quote_press, text='more_quote')
    dp.register_message_handler(process_chat_gpt_command, Text(startswith=['gpt', 'chatgpt'], ignore_case=True))
