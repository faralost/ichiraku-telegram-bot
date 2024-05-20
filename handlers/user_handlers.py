from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from database.database import ALL_CHATS, add_chat_to_all_chats_db, update_all_chats_db
from external_services.api_ninjas import collect_fact
from external_services.imagekit import get_random_photo_url, ImageKitFolder
from external_services.openai import get_openai_response
from external_services.openweather import collect_weather
from external_services.waifu import collect_quote
from keyboards.keyboards import fact_keyboard, quote_keyboard, photos_keyboard, weather_keyboard
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
    quote = await collect_quote()
    await message.reply(text=quote, reply_markup=quote_keyboard)


async def process_more_quote_press(callback: CallbackQuery):
    await callback.answer()
    quote = await collect_quote()
    await callback.message.reply(text=quote, reply_markup=quote_keyboard)


async def process_chat_gpt_command(message: Message):
    await message.answer_chat_action('typing')
    text = message.text.split(' ', 1)[1]
    response = get_openai_response(text)
    await message.reply(response)


async def process_sakura_command(message: Message):
    await message.reply_photo(
        f'{get_random_photo_url(ImageKitFolder.SAKURA)}',
        caption=LEXICON_RU['sakura_caption'],
        reply_markup=photos_keyboard
    )


async def process_more_sakura_press(callback: CallbackQuery):
    await callback.answer()
    await callback.message.reply_photo(
        f'{get_random_photo_url(ImageKitFolder.SAKURA)}',
        caption=LEXICON_RU['sakura_caption'],
        reply_markup=photos_keyboard
    )


async def process_kakura_command(message: Message):
    await message.reply_photo(
        f'{get_random_photo_url(ImageKitFolder.KAKURA)}',
        caption=LEXICON_RU['kakura_caption'],
        reply_markup=photos_keyboard
    )


async def process_more_kakura_press(callback: CallbackQuery):
    await callback.answer()
    await callback.message.reply_photo(
        f'{get_random_photo_url(ImageKitFolder.KAKURA)}',
        caption=LEXICON_RU['kakura_caption'],
        reply_markup=photos_keyboard
    )


async def process_wedding_command(message: Message):
    await message.reply_photo(
        f'{get_random_photo_url(ImageKitFolder.WEDDING)}',
        caption=LEXICON_RU['wedding_caption'],
        reply_markup=photos_keyboard
    )


async def process_more_wedding_press(callback: CallbackQuery):
    await callback.answer()
    await callback.message.reply_photo(
        f'{get_random_photo_url(ImageKitFolder.WEDDING)}',
        caption=LEXICON_RU['wedding_caption'],
        reply_markup=photos_keyboard
    )


async def process_weather_press(callback: CallbackQuery):
    await callback.answer()
    text = LEXICON_RU['todays_weather'] + await collect_weather()
    await callback.message.reply(text=text, reply_markup=weather_keyboard)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_fact_command, commands='fact')
    dp.register_callback_query_handler(process_more_fact_press, text='more_fact')
    dp.register_message_handler(process_quote_command, commands='quote')
    dp.register_callback_query_handler(process_more_quote_press, text='more_quote')
    dp.register_message_handler(process_chat_gpt_command, Text(startswith=['gpt', 'chatgpt'], ignore_case=True))
    dp.register_message_handler(process_sakura_command, commands='sakura')
    dp.register_callback_query_handler(process_more_sakura_press, text='sakura')
    dp.register_message_handler(process_kakura_command, commands='kakura')
    dp.register_callback_query_handler(process_more_kakura_press, text='kakura')
    dp.register_message_handler(process_wedding_command, commands='wedding')
    dp.register_callback_query_handler(process_more_wedding_press, text='wedding')
    dp.register_callback_query_handler(process_weather_press, text='weather')
