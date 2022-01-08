
import numpy as np

class TechnicalIndicators:

    def __init__(self):
        pass

    @staticmethod
    async def calculate_all_emas(ticker_df):
        emas = [9, 21, 50, 90, 200]
        for ma in emas:
            ticker_df[f'{ma}_EMA'] = ticker_df.loc[:, 'Close'].ewm(span=ma, min_periods=ma,
                                                                   adjust=False).mean()
        return ticker_df

    @staticmethod
    async def calculate_all_vwma(ticker_df):
        emas = [9, 21, 50, 90, 200]
        for ma in emas:
            rolling_close = ticker_df['Close'].rolling(ma)
            rolling_volumne = ticker_df['Volume'].rolling(ma)
            ticker_df[f'{ma}_VWMA'] = ticker_df.rolling(ma).apply(lambda x: np.sum(x['Volume'] * x['Close']))
        return ticker_df
