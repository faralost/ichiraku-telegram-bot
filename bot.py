import asyncio
import logging

from aiogram import Bot, Dispatcher, executor

from config_data import config
from handlers.game_handlers import register_game_handlers
from handlers.scheduled_tasks import scheduler
from handlers.user_handlers import register_user_handlers
from handlers.other_handlers import register_other_handlers
from keyboards.set_menu import set_main_menu

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
)


def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_game_handlers(dp)
    register_other_handlers(dp)


async def on_startup(dp: Dispatcher):
    logger.info('Starting bot...')
    await set_main_menu(dp)
    register_all_handlers(dp)
    asyncio.create_task(scheduler(bot))


if __name__ == '__main__':
    try:
        bot: Bot = Bot(token=config.BOT_API_TOKEN, parse_mode='HTML')
        dp: Dispatcher = Dispatcher(bot)
        executor.start_polling(dp, on_startup=on_startup)
    except (KeyboardInterrupt, SystemExit) as e:
        logger.error('Bot stopped!', e)
