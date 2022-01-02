
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
            print("Getting Tickers")
            all_tickers = self.scanner.get_all_tickers()
            print(f"Tickers available: {len(all_tickers)}")
            text = f"Scanning in {len(all_tickers)} stocks"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            print("Scanning for All Time High")
            tickers = await self.scanner.get_all_time_high_st(update, context, all_tickers=all_tickers)
            print("Returning result")
            return tickers
        except Exception as e:
            print(traceback.print_exc())
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def ath_long(self):
        try:
            print("Getting Tickers")
            all_tickers = self.scanner.get_all_tickers()
            print(f"Tickers available: {len(all_tickers)}")
            print("Scanning for All Time High")
            tickers = await self.scanner.get_all_time_high_lt(all_tickers=all_tickers)
            print("Returning result")
            return tickers
        except Exception as e:
            print(traceback.print_exc())
