
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from Code.Utilities.config.config_util import ConfigUtil

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s', level=logging.INFO)

updater = Updater(token=ConfigUtil.get_config('telegram')['stockmarket0796_bot'])

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps)
unknown_handeler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(unknown_handeler)

updater.start_polling()