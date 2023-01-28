from aiogram import Dispatcher, types

from lexicon.lexicon_ru import LEXICON_RU


async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description=LEXICON_RU['start_menu']),
        types.BotCommand(command='/help', description=LEXICON_RU['help_menu']),
        types.BotCommand(command='/fact', description=LEXICON_RU['fact_menu']),
        types.BotCommand(command='/quote', description=LEXICON_RU['quote_menu']),
        types.BotCommand(command='/game', description=LEXICON_RU['game_menu']),
        types.BotCommand(command='/stat', description=LEXICON_RU['stat_menu']),
        types.BotCommand(command='/stats', description=LEXICON_RU['stats_menu']),
        types.BotCommand(command='/sakura', description=LEXICON_RU['sakura']),
        types.BotCommand(command='/kakura', description=LEXICON_RU['kakura']),
        types.BotCommand(command='/wedding', description=LEXICON_RU['wedding']),
    ]
    await dp.bot.set_my_commands(main_menu_commands)
