from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU_INLINE_KB, LEXICON_RU


def create_inline_kb(row_width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    inline_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=row_width)
    if args:
        [
            inline_kb.insert(
                InlineKeyboardButton(text=LEXICON_RU_INLINE_KB[button], callback_data=button))
            for button in args
        ]
    if kwargs:
        [inline_kb.insert(InlineKeyboardButton(text=text, callback_data=button)) for button, text in kwargs.items()]
    return inline_kb


fact_keyboard = create_inline_kb(1, 'more_fact')
quote_keyboard = create_inline_kb(1, 'more_quote')
weather_keyboard = create_inline_kb(1, 'weather')
photos_keyboard = create_inline_kb(2, 'sakura', 'kakura', 'wedding')

admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
admin_kb.add(InlineKeyboardButton(text=LEXICON_RU['ichiraku_message']))
