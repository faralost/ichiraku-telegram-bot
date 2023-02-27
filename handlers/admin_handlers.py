from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message

from config_data import config
from keyboards.keyboards import admin_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.admin_services import get_bot_stats


class Dialog(StatesGroup):
    ichiraku_message = State()
    ichiraku_photo = State()


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
    await bot.send_message(config.ICHIRAKU_CHAT_ID, message.text)
    await message.reply(text=LEXICON_RU['sent'])
    await state.finish()


async def bot_stats(message: Message):
    await message.reply(text=get_bot_stats())


async def ichiraku_photo(message: Message):
    await Dialog.ichiraku_photo.set()
    await message.reply(text=LEXICON_RU['message_photo'])


async def warning_not_photo(message: Message):
    await message.answer(text=LEXICON_RU['warning_not_photo'])


async def start_ichiraku_photo(message: Message, state: FSMContext):
    from bot import bot
    await bot.send_photo(config.ICHIRAKU_CHAT_ID, message.photo[0].file_id, caption=LEXICON_RU['just_photo'])
    await message.reply(text=LEXICON_RU['sent'])
    await state.finish()


async def process_cancel_command(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['quit'])
    await state.reset_state()


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(process_cancel_command, commands='quit', state='*')
    dp.register_message_handler(process_admin_command, commands='admin')
    dp.register_message_handler(ichiraku_message, content_types=['text'], text=LEXICON_RU['ichiraku_message'])
    dp.register_message_handler(ichiraku_photo, content_types=['text'], text=LEXICON_RU['ichiraku_photo'])
    dp.register_message_handler(bot_stats, content_types=['text'], text=LEXICON_RU['admin_stats'])
    dp.register_message_handler(start_ichiraku_message, state=Dialog.ichiraku_message)
    dp.register_message_handler(start_ichiraku_photo, content_types='photo', state=Dialog.ichiraku_photo)
    dp.register_message_handler(warning_not_photo, content_types='any', state=Dialog.ichiraku_photo)

