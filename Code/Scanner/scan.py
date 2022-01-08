"""
author: Kaushal Sharma
date: 2021-12-11
"""
import asyncio
import os
import traceback
import pandas as pd

from telegram.ext import CallbackContext
from telegram import Update, ChatAction

from Code.Core.fetch_data import FetchData
from Code.Core.technical_indicators import TechnicalIndicators
from Code.Core.visualise_data import VisualiseData
from Code.Algorithms.ema_crossover import EmaCrossover
from Code.Core.calc_pl import CalculateProfitLoss
from Code.Algorithms.all_time_high import AllTimeHigh


class Scanner:

    def __init__(self):
        self.sector_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tickers')
        self.all_sector_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'all_sectors')

    async def get_all_time_high_st(self,update: Update, context: CallbackContext):
        try:
            for p,d,f in os.walk(self.sector_path):
                for sector in f:
                    ath_tickers = []
                    if '.csv' not in sector:
                        continue
                    sector_name = sector.split('.')[0].replace('_', ' ')
                    text = f"Scanning sector: {sector_name}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                    for ticker in pd.read_csv(os.path.join(p, sector))['Symbol'].to_list():
                        ath_tickers.append(await AllTimeHigh.close_to_ath_short_term(symbol=ticker))
                    ath_tickers = list(filter(None, ath_tickers))

                    if len(ath_tickers) <= 0:
                        text = f"No stocks near All Time High in sector: {sector_name}"
                    else:
                        text = f"{len(ath_tickers)} stocks identified close to " \
                               f"All Time High in the sector: {sector_name}\n\n"
                        for ticker in ath_tickers:
                            text += str(ticker)+"\n"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        except Exception as e:
            print(f"Error occured: {e}")
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def get_all_time_high_lt(self,update: Update, context: CallbackContext):
        try:
            for p,d,f in os.walk(self.sector_path):
                for sector in f:
                    ath_tickers = []
                    if '.csv' not in sector:
                        continue
                    sector_name = sector.split('.')[0].replace('_', ' ')
                    text = f"Scanning sector: {sector_name}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                    for ticker in pd.read_csv(os.path.join(p, sector))['Symbol'].to_list():
                        ath_tickers.append(await AllTimeHigh.close_to_ath_long_term(symbol=ticker))
                    ath_tickers = list(filter(None, ath_tickers))

                    if len(ath_tickers) <= 0:
                        text = f"No stocks near All Time High in sector: {sector_name}"
                    else:
                        text = f"{len(ath_tickers)} stocks identified close to " \
                               f"All Time High in the sector: {sector_name}\n\n"
                        for ticker in ath_tickers:
                            text += str(ticker)+"\n"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        except Exception as e:
            print(f"Error occured: {e}")
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def get_9_21_ema_cross(self,update: Update, context: CallbackContext):
        try:
            for p,d,f in os.walk(self.all_sector_path):
                for sector in f:
                    ath_tickers = []
                    if '.csv' not in sector:
                        continue
                    sector_name = sector.split('.')[0].replace('_', ' ')
                    text = "="*5 + f" Scanning sector: {sector_name} " + "="*5
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                    for ticker in pd.read_csv(os.path.join(p, sector))['Symbol'].to_list():
                        ticker_df = await FetchData.fetch_yahoo_fin_data(ticker=ticker, interval='1h', period='6mo')
                        ticker_df = await TechnicalIndicators.calculate_all_emas(ticker_df)
                        ticker_df = await EmaCrossover.identify_9_21_crossover(ticker_df=ticker_df)
                        last_5_days = ticker_df.tail(5)['SIGNAL'].to_list()
                        if 'BUY' in last_5_days and 'SELL' not in last_5_days:
                            ath_tickers.append(ticker)
                        else:
                            continue
                        # ath_tickers.append(await AllTimeHigh.close_to_ath_long_term(symbol=ticker))
                    ath_tickers = list(filter(None, ath_tickers))

                    if len(ath_tickers) <= 0:
                        text = f"No stocks have 9 and 21 EMA Cross in the past " \
                               f"5 days for sector: {sector_name}"
                    else:
                        text = f"{len(ath_tickers)} stocks identified having 9 and 21 EMA Cross in the past " \
                               f"5 days in the sector: {sector_name}\n\n"
                        for ticker in ath_tickers:
                            text += str(ticker)+"\n"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        except Exception as e:
            print(f"Error occured: {e}")
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    async def get_21_90_ema_cross(self,update: Update, context: CallbackContext):
        try:
            for p,d,f in os.walk(self.sector_path):
                for sector in f:
                    ath_tickers = []
                    if '.csv' not in sector:
                        continue
                    sector_name = sector.split('.')[0].replace('_', ' ')
                    text = f"Scanning sector: {sector_name}"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
                    for ticker in pd.read_csv(os.path.join(p, sector))['Symbol'].to_list():
                        ticker_df = await FetchData.fetch_yahoo_fin_data(ticker=ticker, interval='1d', period='1y')
                        ticker_df = await TechnicalIndicators.calculate_all_emas(ticker_df)
                        ticker_df = await EmaCrossover.identify_21_90_crossover(ticker_df=ticker_df)
                        last_3_days = ticker_df.tail(3)['SIGNAL'].to_list()
                        if 'BUY' in last_3_days and 'SELL' not in last_3_days:
                            ath_tickers.append(ticker)
                        else:
                            continue
                        # ath_tickers.append(await AllTimeHigh.close_to_ath_long_term(symbol=ticker))
                    ath_tickers = list(filter(None, ath_tickers))

                    if len(ath_tickers) <= 0:
                        text = f"No stocks have 21 and 90 EMA Cross in the past " \
                               f"3 days for sector: {sector_name}"
                    else:
                        text = f"{len(ath_tickers)} stocks identified having 21 and 90 EMA Cross in the past " \
                               f"3 days in the sector: {sector_name}\n\n"
                        for ticker in ath_tickers:
                            text += str(ticker)+"\n"
                    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        except Exception as e:
            print(f"Error occured: {e}")
            text = f"Sorry i could not process the request\nError: {e}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)



if __name__ == '__main__':
    try:
        # scanner = Scanner()
        # for p, d, f in os.walk(scanner.sector_path):
        #     for sector in f:
        #         ath_tickers = []
        #         if '.csv' not in sector:
        #             continue
        #         sector_name = sector.split('.')[0].replace('_', ' ')
        #         text = f"Scanning sector: {sector_name}"
        #         for ticker in pd.read_csv(os.path.join(p, sector))['Symbol'].to_list():
        #             print(f"Looking up: {ticker}")
        #             ticker_df = asyncio.run(FetchData.fetch_yahoo_fin_data(ticker=ticker, interval='1d', period='1y'))
        #             ticker_df = asyncio.run(TechnicalIndicators.calculate_all_emas(ticker_df))
        #             ticker_df = asyncio.run(EmaCrossover.identify_21_90_crossover(ticker_df=ticker_df))
        #             ticker_df = CalculateProfitLoss.calculate_pl(ticker_df=ticker_df)
        #             print("="*60)
        ticker_df = asyncio.run(FetchData.fetch_yahoo_fin_data(ticker='ITC', interval='1d', period='1y'))
        ticker_df = asyncio.run(TechnicalIndicators.calculate_all_emas(ticker_df))
        ticker_df = asyncio.run(TechnicalIndicators.calculate_all_vwma(ticker_df=ticker_df))
        ticker_df = asyncio.run(EmaCrossover.identify_21_90_crossover(ticker_df=ticker_df))
        ticker_df = CalculateProfitLoss.calculate_pl(ticker_df=ticker_df)
    except Exception as e:
        print(f"Error ocurred: {e}")
    #     available_tickers = Scanner.get_all_tickers()
    #     # for key, value in available_tickers.items():
    #     #     print(key, value)
    #
    #     # selection = int(input("\nWhich sector would you like to scan?\n"))
    #     selection = 3
    #     print(f'{available_tickers[selection]} selected\n')
    #     sector_selected = os.path.join('tickers', available_tickers[selection].replace(' ', '_') + '.csv')
    #     sector_df = pd.read_csv(sector_selected)
    #
    #     timeintervals = {
    #         1: '1m',
    #         2: '2m',
    #         3: '5m',
    #         4: '15m',
    #         5: '30m',
    #         6: '60m',
    #         7: '90m',
    #         8: '1h',
    #         9: '1d',
    #         10: '5d',
    #         11: '1w',
    #         12: '1mo',
    #         13: '3mo',
    #     }
    #
    #     # for key, value in timeintervals.items():
    #     #     print(key, value)
    #
    #     # userIntervalSelection = int(input("\nWhat candle interval you want to look at?(default is 1d)\n"))
    #     userIntervalSelection = 4
    #     interval = timeintervals[userIntervalSelection]
    #
    #     if userIntervalSelection <= 5:
    #         timeperiod = {
    #             1: '1d',
    #             2: '5d',
    #             3: '1mo',
    #         }
    #     else:
    #         timeperiod = {
    #             1: '1d',
    #             2: '5d',
    #             3: '1mo',
    #             4: '3mo',
    #             5: '6mo',
    #             6: '1y',
    #             7: '2y',
    #             8: '5y',
    #             9: '10y',
    #             10: 'ytd',
    #             11: 'max',
    #         }
    #
    #     # for key, value in timeperiod.items():
    #     #     print(key, value)
    #
    #     # period = timeperiod[int(input("\nAcross what time period do you "
    #     #                               "wanna analyse the stock?(default is 1mo)\n"))]
    #     period = timeperiod[3]
    #
    #     for index, row in sector_df.iterrows():
    #         symbol = row['Symbol']
    #         if 'NIFTY' in symbol.split(' '):
    #             continue
    #         try:
    #             print("=" * 100)
    #             print(f"Scanning {symbol}")
    #             # symbol_data = asyncio.run(
    #             #     FetchData.fetch_yahoo_fin_data(ticker=symbol, period=period, interval=interval))
    #             # symbol_data.drop(['Open', 'High', 'Low', 'Adj Close'], axis=1, inplace=True)
    #             # symbol_data.reset_index(drop=False, inplace=True)
    #             # ticker_df = asyncio.run(TechnicalIndicators.calculate_all_emas(symbol_data))
    #             # # ticker_df = asyncio.run(EmaCrossover.identify_crossovers_close_9ema(ticker_df=ticker_df))
    #             # ticker_df = asyncio.run(EmaCrossover.identify_9_21_crossover(ticker_df=ticker_df))
    #             # ticker_df = CalculateProfitLoss.calculate_pl(ticker_df=ticker_df)
    #             asyncio.run(AllTimeHigh.close_to_ath_short_term(symbol=symbol))
    #             asyncio.run(AllTimeHigh.close_to_ath_long_term(symbol=symbol))
    #
    #             # break
    #         except Exception as e:
    #             print(f"Error in processing or data not available for {symbol}")
    #
    # except Exception as e:
    #     print(e)
    #     print(traceback.print_exc())
