
import asyncio

import Code.TelegramBot.telegram_util as util
from telegram.ext import CallbackContext, Filters, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, ReplyKeyboardMarkup, utils, InlineKeyboardMarkup, ChatAction

from Code.TelegramBot.telegram_services import TelegramServices


class TelegramCommands:

    def __init__(self):
        pass

    @staticmethod
    def start(update: Update, context: CallbackContext):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
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
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        query = update.callback_query
        query.answer()
        service = query.data
        telegram_services = TelegramServices()

        try:
            if service == 'ath_short':
                text = "Finding stocks close to All Time High in Short Term\n\n"
                text += "interval: 1 hour\nperiod: 6 months\n\nThis might take some time"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

                try:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    asyncio.run(telegram_services.ath_short(update, context))
                    text = f"Scanning Complete"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                except Exception as e:
                    text = f"Sorry i could not process the request\nError: {e}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

            elif service == 'ath_long':
                text = "Finding stocks close to All Time High in Long Term\n\n"
                text += "interval: 1 month\nperiod: MAX\n this might take some time"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

                try:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    asyncio.run(telegram_services.ath_long(update, context))
                    text = f"Scanning Complete"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                except Exception as e:
                    text = f"Sorry i could not process the request\nError: {e}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

            else:
                text = "I could not find the selected service"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        except Exception as e:
            text = f"Sorry, i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)


    @staticmethod
    def unknown(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm sorry I don't understand that command")