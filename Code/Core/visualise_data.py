
import matplotlib.pyplot as plt
import pandas as pd


class VisualiseData:

    def __init__(self):
        pass

    @staticmethod
    def plot_close_price(ticker_df, symbol:str):
        # ticker_df.set_index(pd.DatetimeIndex(ticker_df['Date'].values), inplace=True)
        plt.figure(figsize=(14,8))
        plt.title(f'{symbol}', fontsize=18)
        plt.plot(ticker_df['Close'])
        plt.xlabel('Date', fontsize=13)
        plt.ylabel('Close price', fontsize=13)
        plt.show()

    @staticmethod
    def plot_emas(ticker_df, symbol:str):
        pass

    @staticmethod
    def plot_signals(ticker_df, symbol:str):
        pass
