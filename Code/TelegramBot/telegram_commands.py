
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
            InlineKeyboardButton(text="9-21 EMA Cross", callback_data="9_21_ema_cross"),
            InlineKeyboardButton(text="21-90 EMA Cross (30 Mins)", callback_data="21_90_ema_cross_30mins"),
            InlineKeyboardButton(text="21-90 EMA Cross (1 Hour)", callback_data="21_90_ema_cross_1hour"),
            InlineKeyboardButton(text="21-90 EMA Cross (1 Day)", callback_data="21_90_ema_cross_1day"),
            InlineKeyboardButton(text="21-200 EMA Cross\n(Short Term)", callback_data="21_200_ema_cross_st"),
            InlineKeyboardButton(text="21-200 EMA Cross\n(Long Term)", callback_data="21_200_ema_cross_lt"),
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
                    text = "="*10 + "Scanning Complete" + "="*10
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
                    text = "="*10 + "Scanning Complete" + "="*10
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                except Exception as e:
                    text = f"Sorry i could not process the request\nError: {e}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

            elif service == '9_21_ema_cross':
                text = "Finding stocks with 9 and 21 EMA Crossing\n\n"
                text += "interval: 1 Hour\nperiod: 1 Month\n\nThis might take some time"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

                try:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    asyncio.run(telegram_services.ema_cross_9_21(update, context))
                    text = "="*10 + "Scanning Complete" + "="*10
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                except Exception as e:
                    text = f"Sorry i could not process the request\nError: {e}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

            elif service == '21_90_ema_cross_30min':
                text = "Finding stocks with 21 and 90 EMA Crossing\n\n"
                text += "interval: 30 Mins \nperiod: 1 Month\n\nThis might take some time"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

                try:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    asyncio.run(telegram_services.ema_cross_21_90_30m(update, context))
                    text = "="*10 + "Scanning Complete" + "="*10
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                except Exception as e:
                    text = f"Sorry i could not process the request\nError: {e}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

            elif service == '21_90_ema_cross_1hour':
                text = "Finding stocks with 21 and 90 EMA Crossing\n\n"
                text += "interval: 1 Hour \nperiod: 1 Month\n\nThis might take some time"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

                try:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    asyncio.run(telegram_services.ema_cross_21_90_1h(update, context))
                    text = "="*10 + "Scanning Complete" + "="*10
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                except Exception as e:
                    text = f"Sorry i could not process the request\nError: {e}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

            elif service == '21_90_ema_cross_1day':
                text = "Finding stocks with 21 and 90 EMA Crossing\n\n"
                text += "interval: 1 Day\nperiod: 1 Month\nThis might take some time"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

                try:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    asyncio.run(telegram_services.ema_cross_21_90_1d(update, context))
                    text = "="*10 + "Scanning Complete" + "="*10
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                except Exception as e:
                    text = f"Sorry i could not process the request\nError: {e}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

            elif service == '21_200_ema_cross_st':
                text = "Finding stocks with 21 and 200 EMA Crossing for Short Term\n\n"
                text += "interval: 30 minutes\nperiod: 1 Month\n\nThis might take some time"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

                try:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    asyncio.run(telegram_services.ema_cross_21_200_short_term(update, context))
                    text = "="*10 + "Scanning Complete" + "="*10
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                except Exception as e:
                    text = f"Sorry i could not process the request\nError: {e}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

            elif service == '21_200_ema_cross_lt':
                text = "Finding stocks with 21 and 200 EMA Crossing for Long Term\n\n"
                text += "interval: 1 hour\nperiod: 1 Month\n\nThis might take some time"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)

                try:
                    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
                    asyncio.run(telegram_services.ema_cross_21_200_long_term(update, context))
                    text = "="*10 + "Scanning Complete" + "="*10
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