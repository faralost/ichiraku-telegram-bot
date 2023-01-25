import asyncio

import aioschedule

from database.database import ALL_CHATS
from keyboards.keyboards import keyboard
from services.fact_services import collect_fact
from services.services import send_to_all_chats


async def send_fact():
    from bot import bot
    text = f"*Рандомный факт дня* 📰\n\n"
    text += await collect_fact()
    await send_to_all_chats(ALL_CHATS, bot, text, reply_markup=keyboard)


async def scheduler():
    aioschedule.every().day.at('22:20').do(send_fact)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
