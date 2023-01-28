from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon_ru import LEXICON_RU

fact_keyboard = InlineKeyboardMarkup()
fact_button = InlineKeyboardButton(text=LEXICON_RU['more_fact'], callback_data='more_fact')
fact_keyboard.add(fact_button)

quote_keyboard = InlineKeyboardMarkup()
quote_button = InlineKeyboardButton(text=LEXICON_RU['more_quote'], callback_data='more_quote')
quote_keyboard.add(quote_button)

photos_keyboard = InlineKeyboardMarkup(row_width=2)
sakura_button = InlineKeyboardButton(text=LEXICON_RU['sakura'], callback_data='more_sakura')
kakura_button = InlineKeyboardButton(text=LEXICON_RU['kakura'], callback_data='more_kakura')
wedding_button = InlineKeyboardButton(text=LEXICON_RU['wedding'], callback_data='more_wedding')
photos_keyboard.add(sakura_button, kakura_button, wedding_button)
