import pickle

with open('database/pickle_db', 'rb') as file:
    ALL_CHATS: set[int] = pickle.load(file)


def add_chat_to_all_chats_db(chat_id: int) -> None:
    ALL_CHATS.add(chat_id)


def update_all_chats_db(chats: set[int]) -> None:
    with open('database/pickle_db', 'wb') as f:
        pickle.dump(chats, f)

