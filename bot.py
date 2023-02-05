import asyncio
import logging

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config_data import config
from handlers.admin_handlers import register_admin_handlers
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

sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)
sentry_sdk.init(
    dsn=config.SENTRY_DSN,
    integrations=[sentry_logging],
    traces_sample_rate=1.0,
    attach_stacktrace=True,
)

storage = MemoryStorage()

bot: Bot = Bot(token=config.BOT_API_TOKEN, parse_mode='HTML')
dp: Dispatcher = Dispatcher(bot, storage=storage)


def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_game_handlers(dp)
    register_admin_handlers(dp)
    register_other_handlers(dp)


async def on_startup(dp: Dispatcher):
    logger.info('Starting bot...')
    await set_main_menu(dp)
    register_all_handlers(dp)
    asyncio.create_task(scheduler(bot))


if __name__ == '__main__':
    try:
        executor.start_polling(dp, on_startup=on_startup)
    except (KeyboardInterrupt, SystemExit) as e:
        logger.error('Bot stopped!', e)
