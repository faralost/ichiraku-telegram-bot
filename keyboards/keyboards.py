from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from lexicon.lexicon_ru import LEXICON_RU

fact_keyboard = InlineKeyboardMarkup()
fact_button = InlineKeyboardButton(text=LEXICON_RU['more_fact'], callback_data='more_fact')
fact_keyboard.add(fact_button)

quote_keyboard = InlineKeyboardMarkup()
quote_button = InlineKeyboardButton(text=LEXICON_RU['more_quote'], callback_data='more_quote')
quote_keyboard.add(quote_button)
