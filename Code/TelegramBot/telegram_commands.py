
import Code.TelegramBot.telegram_util as util
from telegram.ext import CallbackContext, Filters, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, ReplyKeyboardMarkup, utils, InlineKeyboardMarkup

from Code.TelegramBot.telegram_services import TelegramServices

class TelegramCommands:

    def __init__(self):
        pass

    @staticmethod
    def start(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm StockBot!")

    @staticmethod
    def menu(update: Update, context: CallbackContext):
        services_available = [
            InlineKeyboardButton(text="All Time High (Short Term)", callback_data="ath_short"),
            InlineKeyboardButton(text="All Time High (Long Term)", callback_data="ath_long"),
        ]
        reply_markup = InlineKeyboardMarkup(util.build_menu(services_available, n_cols=2))
        context.bot.send_message(chat_id=update.message.chat_id, text="Below are the live services",
                                 reply_markup=reply_markup)

    @staticmethod
    def menuclick(update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        service = query.data
        if service == 'ath_short':
            text = TelegramServices.ath_short()
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        elif service == 'ath_long':
            text = TelegramServices.ath_long()
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        else:
            text = "I could not find the selected service"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    @staticmethod
    def unknown(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm sorry I don't understand that command")