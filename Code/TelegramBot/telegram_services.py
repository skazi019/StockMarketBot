
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
