import pickle


BIRTHDAYS = {
    '03-01': 'Сайкал',
    '17-01': 'Карина',
    '27-01': 'Надира',
    '14-02': 'Жакшыбай',
    '07-05': 'Атакан',
    '30-07': 'Эмир',
    '05-09': 'Нургиза',
    '28-10': 'Айжан',
    '22-11': 'Фархатжан',
    '25-11': 'Ильяс',
    '26-01': 'Ильяс',
}

with open('database/pickle_db', 'rb') as file:
    ALL_CHATS: set[int] = pickle.load(file)


def add_chat_to_all_chats_db(chat_id: int) -> None:
    ALL_CHATS.add(chat_id)


def update_all_chats_db(chats: set[int]) -> None:
    with open('database/pickle_db', 'wb') as f:
        pickle.dump(chats, f)

