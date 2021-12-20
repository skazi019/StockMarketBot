"""
author: Kaushal Sharma
date: 2021-12-11
"""
import asyncio
import os
import traceback
import pandas as pd

from Code.Core.fetch_data import FetchData
from Code.Core.technical_indicators import TechnicalIndicators
from Code.Core.visualise_data import VisualiseData


class Scanner:

    def __init__(self):
        pass

    def get_all_tickers():
        counter = 1
        ticker_selection = {}
        for files in os.listdir('tickers'):
            files = files.split('.')[0].replace('_', ' ')
            ticker_selection[counter] = files
            counter += 1
        return ticker_selection


try:
    available_tickers = Scanner.get_all_tickers()
    # for key, value in available_tickers.items():
    #     print(key, value)

    # selection = int(input("\nWhich sector would you like to scan?\n"))
    selection = 3
    print(f'{available_tickers[selection]} selected\n')
    sector_selected = 'tickers/' + available_tickers[selection].replace(' ', '_') + '.csv'
    sector_df = pd.read_csv(sector_selected)

    timeintervals = {
        1: '1m',
        2: '2m',
        3: '5m',
        4: '15m',
        5: '30m',
        6: '60m',
        7: '90m',
        8: '1h',
        9: '1d',
        10: '5d',
        11: '1w',
        12: '1mo',
        13: '3mo',
    }

    # for key, value in timeintervals.items():
    #     print(key, value)

    # userIntervalSelection = int(input("\nWhat candle interval you want to look at?(default is 1d)\n"))
    userIntervalSelection = 4
    interval = timeintervals[userIntervalSelection]

    if userIntervalSelection <= 5:
        timeperiod = {
            1: '1d',
            2: '5d',
            3: '1mo',
        }
    else:
        timeperiod = {
            1: '1d',
            2: '5d',
            3: '1mo',
            4: '3mo',
            5: '6mo',
            6: '1y',
            7: '2y',
            8: '5y',
            9: '10y',
            10: 'ytd',
            11: 'max',
        }

    # for key, value in timeperiod.items():
    #     print(key, value)

    # period = timeperiod[int(input("\nAcross what time period do you "
    #                               "wanna analyse the stock?(default is 1mo)\n"))]
    period = timeperiod[3]

    for index, row in sector_df.iterrows():
        symbol = row['Symbol']
        if symbol == 'NIFTY 50':
            continue
        try:
            print(f"Scanning {symbol}")
            symbol_data = asyncio.run(FetchData.fetch_yahoo_fin_data(ticker=symbol, period=period, interval=interval))
            ticker_df = asyncio.run(TechnicalIndicators.calculate_all_emas(symbol_data))
            VisualiseData.plot_close_price(ticker_df=ticker_df, symbol=symbol)



            break
        except Exception as e:
            print(f"Error in processing or data not available for {symbol}")

except Exception as e:
    print(e)
    print(traceback.print_exc())