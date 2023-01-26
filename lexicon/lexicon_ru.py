import random
from typing import TypedDict

from services.game_services import ATTEMPTS

EMOJIS = ('🌞', '🌝', '🌼', '🌷', '🥰', '😇', '🌻', '🌸', '🍀', '☀️', '🍳', '☕️',)


class Lexicon(TypedDict):
    start: str
    help: str
    smile: str
    more_fact: str
    more_quote: str
    quote_of_the_day: str
    fact_of_the_day: str
    anime: str
    character: str
    asia_bishkek: str
    asia_almaty: str
    asia_novosibirsk: str
    min_temp: str
    max_temp: str
    good_morning: str
    todays_weather: str
    birthday_text: str
    game: str
    not_in_game: str
    games_played: str
    game_wins: str
    game_losses: str
    player: str
    stat: str


LEXICON_RU: Lexicon = {
    'start': "<b>Привет!👋 Я бот Ичираку🍥</b>\n\n"
             "<i>В целом я пока мало что умею, но я развиваюсь и совершенствуюсь каждый день</i>🤖\n\n"
             "Посмотреть что умею: /help\n\n"
             "По вопросам сюда: <tg-spoiler>@faralost</tg-spoiler>",
    'help': "/sakura - Фото Сакуры🐈\n"
            "/kakura - Фото Какуры🐒\n"
            "/fact - Интересный факт📰\n"
            "/quote - Цитата из Аниме🍥\n"
            "/wedding - Фотка со свадьбы Эмира и Айжан🕺💃\n"
            "/game - Сыграть в Угадай Число🎮\n\n"
            "-Начни запрос со слова <i><b>gpt</b></i> и тебе ответит нейронка OpenAI💻\n"
            "-Любое другое написанное вами мне я вам просто отзеркалю🪞",
    'smile': '\n😁<i>улыбок тебе дед мокар</i>😁',
    'more_fact': 'Хочу еще факт!📰',
    'more_quote': 'Хочу еще цитату!💬',
    'quote_of_the_day': "*Цитата дня из Аниме* 💬\n\n",
    'fact_of_the_day': "*Рандомный факт дня* 📰\n\n",
    'anime': "Аниме",
    'character': "Персонаж",
    'Asia/Bishkek': "Бишкек",
    'Asia/Almaty': "Алматы",
    'Asia/Novosibirsk': "Новосибирск",
    'min_temp': "Мин",
    'max_temp': "Макс",
    'good_morning': f'<b>Доброе утро! Отличного Вам дня!</b>{random.choice(EMOJIS)}\n\n',
    'todays_weather': "🌍<i>Погода на сегодня</i>🌏\n\n",
    'birthday_text': f"<b>УРА! ПОЗДРАВЛЯЮ!🥳\n\n"
                     f"Сегодня день рождения у...</b>🥁(<i>барабанная дробь...</i>)\n\n",
    'game': f'<b>Правила игры:</b>\n\n'
            f'Я загадываю число от <b>1</b> до <b>100</b>, а вам нужно его угадать\n'
            f'У вас есть <b>{ATTEMPTS}</b> попыток\n\n'
            f'Доступные команды в игре:\n'
            f'/cancel - выйти из игры\n'
            f'/stat - посмотреть вашу статистику\n'
            f'/stats - посмотреть общую статистику\n\n'
            f'<i>Давай сыграем? Напиши "Давай", "Игра" или "Го" и сразу начнем</i>🎰',
    'not_in_game': 'Вы еще не зарегистрированы в игре😔 Нажмите /game',
    'games_played': '<i>🙌Всего игр</i>',
    'game_wins': '<i>👍Выиграно</i>',
    'game_losses': '<i>👎Проиграно</i>',
    'player': '<b>Игрок</b>',
    'stat': '📊<b>Статистика</b>📊'
}
