import asyncio
import traceback

from Code.Core.fetch_data import FetchData


class AllTimeHigh:

    def __init__(self):
        pass

    @staticmethod
    async def close_to_ath_short_term(symbol: str, interval: str = '1h', period: str = '6mo'):
        try:
            ticker_df = await FetchData.fetch_yahoo_fin_data(ticker=symbol, interval=interval, period=period)
            max_high = max(ticker_df['High'])
            if ticker_df.iloc[-1]['Close'] >= (max_high - (max_high * 0.1)):
                print(f"{symbol} close to SHORT TERM all time high")
            else:
                pass
        except Exception as e:
            print(traceback.print_exc())

    @staticmethod
    async def close_to_ath_long_term(symbol: str, interval: str = '1d', period: str = 'max'):
        ticker_df = await FetchData.fetch_yahoo_fin_data(ticker=symbol, interval=interval, period=period)
        max_high = max(ticker_df['High'])
        if ticker_df.iloc[-1]['Close'] >= (max_high - (max_high * 0.1)):
            print(f"{symbol} close to LONG TERM all time high")
        else:
            pass
