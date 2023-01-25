from typing import TypedDict


class Lexicon(TypedDict):
    start: str
    help: str
    smile: str


LEXICON_RU: Lexicon = {
    'start': "<b>Привет!👋 Я бот Ичираку🍥</b>\n\n"
             "<i>В целом я пока мало что умею, но я развиваюсь и совершенствуюсь каждый день</i>🤖\n\n"
             "Посмотреть что умею: /help\n\n"
             "По вопросам сюда: <tg-spoiler>@faralost</tg-spoiler>",
    'help': "/sakura - Фото Сакуры🐈\n"
            "/kakura - Фото Какуры🐒\n"
            "/fact - Интересный факт📰\n"
            "/naruto - Цитата из Наруто🍥\n"
            "/wedding - Фотка со свадьбы Эмира и Айжан🕺💃\n"
            "/game - Сыграть в Угадай Число🎮\n\n"
            "-Начни запрос со слова <i><b>gpt</b></i> и тебе ответит нейронка OpenAI💻\n"
            "-Любое другое написанное вами мне я вам просто отзеркалю🪞",
    'smile': '\n🤡<i>улыбок тебе дед мокар</i>🤡',
}
