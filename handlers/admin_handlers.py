from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from config_data import config
from keyboards.keyboards import admin_kb
from lexicon.lexicon_ru import LEXICON_RU


class Dialog(StatesGroup):
    ichiraku_message = State()


async def process_admin_command(message: Message):
    if str(message.from_user.id) == config.ADMIN_ID:
        await message.reply(text=LEXICON_RU['admin_hello'], reply_markup=admin_kb)
    else:
        await message.reply(text=LEXICON_RU['unauthorized'])


async def ichiraku_message(message: Message):
    await Dialog.ichiraku_message.set()
    await message.reply(text=LEXICON_RU['message'])


async def start_ichiraku_message(message: Message, state: FSMContext):
    from bot import bot
    if message.text == 'нет':
        await message.reply(text=LEXICON_RU['quit'])
        await state.finish()
    else:
        await bot.send_message(config.ICHIRAKU_CHAT_ID, message.text)
        await message.reply(text=LEXICON_RU['sent'])
        await state.finish()


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(process_admin_command, commands='admin')
    dp.register_message_handler(ichiraku_message, content_types=['text'], text=LEXICON_RU['ichiraku_message'])
    dp.register_message_handler(start_ichiraku_message, state=Dialog.ichiraku_message)
