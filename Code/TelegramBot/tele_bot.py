
import logging
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update

from Code.Utilities.config.config_util import ConfigUtil

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s', level=logging.INFO)

updater = Updater(token=ConfigUtil.get_config('telegram')['stockmarket0796_bot'])

dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm StockBot!")

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    if len(context.args) <= 0:
        text_caps = 'No text given'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def unknown(update: Update, context: CallbackContext):
    text = "Commands available are:\n"
    text += Filters.command
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

start_handler = CommandHandler('start', start)
caps_handler = CommandHandler('caps', caps)
unknown_handeler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(unknown_handeler)

updater.start_polling()