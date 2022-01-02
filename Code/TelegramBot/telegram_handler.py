
import os
os.chdir('../../')

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from Code.Utilities.config.config_util import ConfigUtil
from Code.TelegramBot.telegram_commands import TelegramCommands

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s', level=logging.INFO)

updater = Updater(token=ConfigUtil.get_config('telegram')['stockmarket0796_bot'])

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', TelegramCommands.start)
menu_handler = CommandHandler('menu', TelegramCommands.menu)
unknown_handler = MessageHandler(Filters.command, TelegramCommands.unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(CallbackQueryHandler(TelegramCommands.menuclick))
dispatcher.add_handler(unknown_handler)

updater.start_polling()
