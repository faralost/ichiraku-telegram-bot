from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from database.database import ALL_CHATS, add_chat_to_all_chats_db, update_all_chats_db
from keyboards.keyboards import keyboard
from lexicon.lexicon_ru import LEXICON_RU
from services.fact_services import collect_fact


async def process_start_command(message: Message):
    await message.reply(text=LEXICON_RU['start'])
    add_chat_to_all_chats_db(message.chat.id)
    update_all_chats_db(ALL_CHATS)


async def process_help_command(message: Message):
    await message.reply(text=LEXICON_RU['help'])


async def process_fact_command(message: Message):
    await message.answer_chat_action('typing')
    fact = await collect_fact()
    await message.reply(text=fact, reply_markup=keyboard)


async def process_more_fact_press(callback: CallbackQuery):
    await callback.answer()
    fact = await collect_fact()
    await callback.message.reply(text=fact, reply_markup=keyboard)


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_fact_command, commands='fact')
    dp.register_callback_query_handler(process_more_fact_press, text='more_fact')
