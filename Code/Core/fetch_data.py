"""
author: Kaushal Sharma
date: 2021-11-05
This file fetches data for the specified scrip from the exchange
"""
import yfinance


class FetchData:

    def __init__(self):
        pass

    @staticmethod
    async def fetch_yahoo_fin_data(ticker:str, period:str, interval:str):
        df = yfinance.download(tickers=f"{ticker}.NS", period=f"{period}", interval=f"{interval}")
        return df
