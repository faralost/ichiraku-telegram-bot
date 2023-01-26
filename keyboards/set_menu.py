from aiogram import Dispatcher, types


async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description='Старт/Рестарт бота'),
        types.BotCommand(command='/help', description='Помощь'),
        types.BotCommand(command='/fact', description='Рандомный факт'),
        types.BotCommand(command='/quote', description='Цитата из Aниме'),
        types.BotCommand(command='/game', description='Угадай Число'),
    ]
    await dp.bot.set_my_commands(main_menu_commands)
