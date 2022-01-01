
import asyncio
import logging
import traceback

from Code.Scanner.scan import Scanner


class TelegramServices:

    def __init__(self):
        self.scanner = Scanner()

    async def ath_short(self):
        try:
            print("Getting Tickers")
            all_tickers = self.scanner.get_all_tickers()
            print(f"Tickers available: {len(all_tickers)}")
            print("Scanning for All Time High")
            tickers = await self.scanner.get_all_time_high_st(all_tickers=all_tickers)
            print("Returning result")
            return tickers
        except Exception as e:
            print(traceback.print_exc())

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
