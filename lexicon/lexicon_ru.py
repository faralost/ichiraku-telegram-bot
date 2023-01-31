import random
from typing import TypedDict

EMOJIS = ('🌞', '🌝', '🌼', '🌷', '🥰', '😇', '🌻', '🌸', '🍀', '☀️', '🍳', '☕️',)


class Lexicon(TypedDict):
    start: str
    help: str
    smile: str
    quote_of_the_day: str
    fact_of_the_day: str
    anime: str
    character: str
    min_temp: str
    max_temp: str
    good_morning: str
    todays_weather: str
    birthday_text: str
    game: str
    not_registered_for_game: str
    games_played: str
    game_wins: str
    game_losses: str
    player: str
    stat: str
    stats: str
    start_menu: str
    help_menu: str
    fact_menu: str
    quote_menu: str
    game_menu: str
    stat_menu: str
    stats_menu: str
    canceled_game: str
    not_playing: str
    we_are_playing: str
    new_game: str
    won_the_game: str
    number_is_smaller: str
    number_is_bigger: str
    lose_the_game: str
    sakura_caption: str
    kakura_caption: str
    wedding_caption: str
    test: str


LEXICON_RU: Lexicon = {
    'start': "<b>Привет!👋 Я бот Ичираку🍥</b>\n\n"
             "<i>В целом я пока мало что умею, но я развиваюсь и совершенствуюсь каждый день</i>🤖\n\n"
             "Посмотреть что умею: /help\n\n"
             "По вопросам сюда: <tg-spoiler>@faralost</tg-spoiler>",
    'help': "/sakura - Фото Сакуры🐈\n"
            "/kakura - Фото Какуры💩\n"
            "/fact - Интересный факт📰\n"
            "/quote - Цитата из Аниме🍥\n"
            "/wedding - Фото со свадьбы Эмира и Айжан🕺💃\n"
            "/game - Сыграть в Угадай Число🎮\n\n"
            "-Начни запрос со слова <i><b>gpt</b></i> и тебе ответит нейронка OpenAI💻\n"
            "-Любое другое написанное вами мне я вам просто отзеркалю🪞",
    'smile': '\n😁<i>улыбок тебе дед мокар</i>😁',
    'quote_of_the_day': "<b>Цитата дня из Аниме</b> 💬\n\n",
    'fact_of_the_day': "*Рандомный факт дня* 📰\n\n",
    'anime': "Аниме",
    'character': "Персонаж",
    'min_temp': "Мин",
    'max_temp': "Макс",
    'good_morning': f'<b>Доброе утро! Отличного дня!</b>{random.choice(EMOJIS)}\n\n',
    'todays_weather': "🌍<i>Погода на сегодня</i>🌏\n\n",
    'birthday_text': "<b>УРА! ПОЗДРАВЛЯЮ!🥳\n\n"
                     "Сегодня день рождения у...</b>🥁(<i>барабанная дробь...</i>)\n\n",
    'game': '<b>Правила игры:</b>\n\n'
            'Я загадываю число от <b>1</b> до <b>100</b>, а вам нужно его угадать🤔\n'
            'У вас есть <b>5</b> попыток\n\n'
            'Доступные команды в игре:\n'
            '/cancel - выйти из игры❌\n'
            '/stat - Ваша статистика📊\n'
            '/stats - Общая статистика📊\n\n'
            '<i>Давай сыграем? Напиши "Давай", "Игра" или "Го" и сразу начнем</i>🎰',
    'not_registered_for_game': 'Вы еще не зарегистрированы в игре😔 Нажмите /game',
    'games_played': '<i>🙌Всего игр</i>',
    'game_wins': '<i>👍Выиграно</i>',
    'game_losses': '<i>👎Проиграно</i>',
    'player': '<b>Игрок</b>',
    'stat': '📊<b>Статистика</b>📊',
    'stats': '📊<b>Статистика</b>📊',
    'start_menu': 'Старт/Рестарт бот🤖',
    'help_menu': 'Помощь❓',
    'fact_menu': 'Рандомный факт📰',
    'quote_menu': 'Цитата из Aниме💬',
    'game_menu': 'Угадай Число🎮',
    'stat_menu': 'Ваша Статистика📊',
    'stats_menu': 'Общая Статистика📊',
    'canceled_game': 'Вы вышли из игры😔 Если захотите сыграть снова, дайте знать😉',
    'not_playing': 'Мы с вами не играем😅 Может, сыграем разок?',
    'we_are_playing': 'Пока мы в игре я могу реагировать только на числа от <b>1</b> до <b>100</b>🤓',
    'new_game': '👾Ура!👾\n\nЯ загадал число от <b>1</b> до <b>100</b>, попробуй угадать!🃏',
    'won_the_game': '👾Ура!!!👾 Вы угадали число!🏆\n\n'
                    'Может сыграем еще?🤩\n\n'
                    '/stat - Ваша статистика📊\n'
                    '/stats - Общая статистика📊',
    'number_is_smaller': 'Мое число меньше⬇️\n'
                         'Попыток осталось: ',
    'number_is_bigger': 'Мое число БОЛЬШЕ⬆️\n'
                        'Попыток осталось: ',
    'lose_the_game': 'К сожалению, у вас больше не осталось попыток😔\n'
                     'Вы проиграли 🥺\n\n'
                     'Давайте сыграем еще?\n'
                     '/stat - Ваша статистика📊\n'
                     '/stats - Общая статистика📊\n\n'
                     '<b>Мое число было</b> ',
    'sakura_caption': 'Бэнг! Бэнг! Сакура в здании!😺',
    'kakura_caption': 'Бэнг! Бэнг! Kакура в здании!😽',
    'wedding_caption': 'Какой прекрасный день!💃🕺',
    'test': 'тест',
}

LEXICON_RU_CITIES = {
    'Asia/Bishkek': "Бишкек",
    'Asia/Almaty': "Алматы",
    'Asia/Novosibirsk': "Новосибирск",
}

LEXICON_RU_INLINE_KB = {
    'sakura': 'Фото Сакуры🐈',
    'kakura': 'Фото Какуры💩',
    'wedding': 'Фото со свадьбы🕺💃',
    'more_fact': 'Хочу еще факт!📰',
    'more_quote': 'Хочу еще цитату!💬',
    'weather': 'Запросить погоду🌡',
}
