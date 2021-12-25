import pandas as pd


class CalculateProfitLoss:

    def __init__(self):
        pass

    @staticmethod
    def calculate_pl(ticker_df):
        ticker_df['BACKTEST_PL'] = 0
        ticker_df['BACKTEST_PL'] = ticker_df.apply(
            lambda x: -x['Close'] if x['SIGNAL'] == 'BUY' else x['Close'] if x['SIGNAL'] == 'SELL' else 0
            , axis=1)
        ticker_df['BACKTEST_PL'] = ticker_df['Close'].diff(periods=1).mask(ticker_df['SIGNAL'] == 'BUY')
        ticker_df['BACKTEST_PL'].fillna(0, inplace=True)
        print(f"\nTotal Profit: {ticker_df['BACKTEST_PL'].sum()}")
        print(f"Winning Trades: {len(ticker_df[ticker_df['BACKTEST_PL'] > 0])}")
        print(f"Losing Trades: {len(ticker_df[ticker_df['BACKTEST_PL'] < 0])}")
        print(f"Max Profit: {max(ticker_df['BACKTEST_PL'])}")
        print(f"Max Loss: {min(ticker_df['BACKTEST_PL'])}")
        return ticker_df
