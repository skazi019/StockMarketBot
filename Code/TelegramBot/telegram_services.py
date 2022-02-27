
import asyncio
import logging
import traceback
from telegram.ext import  CallbackContext
from telegram import  Update

from Code.Scanner.scan import Scanner


class TelegramServices:

    def __init__(self):
        self.scanner = Scanner()

    async def ath_short(self, update: Update, context: CallbackContext):
        try:
            await self.scanner.get_all_time_high_st(update, context)
        except Exception as e:
            print(traceback.print_exc())
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def ath_long(self, update: Update, context: CallbackContext):
        try:
            await self.scanner.get_all_time_high_lt(update, context)
        except Exception as e:
            print(traceback.print_exc())
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def ema_cross_9_21(self, update: Update, context: CallbackContext):
        try:
            await self.scanner.get_9_21_ema_cross(update, context)
        except Exception as e:
            print(traceback.print_exc())
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def ema_cross_21_90_30m(self, update: Update, context: CallbackContext):
        try:
            await self.scanner.get_21_90_ema_cross_30m(update, context)
        except Exception as e:
            print(traceback.print_exc())
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def ema_cross_21_90_1h(self, update: Update, context: CallbackContext):
        try:
            await self.scanner.get_21_90_ema_cross_1h(update, context)
        except Exception as e:
            print(traceback.print_exc())
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def ema_cross_21_90_1d(self, update: Update, context: CallbackContext):
        try:
            await self.scanner.get_21_90_ema_cross_1d(update, context)
        except Exception as e:
            print(traceback.print_exc())
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def ema_cross_21_200_short_term(self, update: Update, context: CallbackContext):
        try:
            await self.scanner.get_21_200_ema_cross_short_term(update, context)
        except Exception as e:
            print(traceback.print_exc())
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def ema_cross_21_200_long_term(self, update: Update, context: CallbackContext):
        try:
            await self.scanner.get_21_200_ema_cross_long_term(update, context)
        except Exception as e:
            print(traceback.print_exc())
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
