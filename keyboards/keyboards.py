from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from lexicon.lexicon_ru import LEXICON_RU

keyboard = InlineKeyboardMarkup()

fact_button = InlineKeyboardButton(text=LEXICON_RU['more_fact'], callback_data='more_fact')
keyboard.add(fact_button)

