import pandas as pd
pd.options.mode.chained_assignment = None


class CalculateProfitLoss:

    def __init__(self):
        pass

    @staticmethod
    def calculate_pl(ticker_df):
        ticker_df.reset_index(drop=False, inplace=True)
        old_ticker_df = ticker_df.copy()
        ticker_df = ticker_df[(ticker_df['SIGNAL'] == 'BUY') | (ticker_df['SIGNAL'] == 'SELL')]
        if ticker_df.head(1)['SIGNAL'].values[0] == 'SELL':
            ticker_df.drop(ticker_df.head(1).index.start, axis=0, inplace=True)
        elif ticker_df.tail(1)['SIGNAL'].values[0] == 'BUY':
            # print("========= Running Profit ==========")
            old_ticker_df.tail(1)['SIGNAL'] = 'SELL'
            ticker_df = pd.concat([ticker_df, old_ticker_df.tail(1)], axis=0)
        else:
            pass

        if len(ticker_df) < 2:
            raise "Not enough data to calculate P/L"
        # ticker_df.loc['BACKTEST_PL'] = 0
        ticker_df.loc[:, 'BACKTEST_PL'] = ticker_df.apply(
            lambda x: -x['Close'] if x['SIGNAL'] == 'BUY' else x['Close'] if x['SIGNAL'] == 'SELL' else 0
            , axis=1)
        ticker_df.loc[:, 'BACKTEST_PL'] = ticker_df['Close'].diff(periods=1).mask(ticker_df['SIGNAL'] == 'BUY').copy()
        ticker_df.loc[:, 'BACKTEST_PL'].fillna(0, inplace=True)
        print(f"\nTotal Profit: {ticker_df['BACKTEST_PL'].sum()}")
        print(f"Winning Trades: {len(ticker_df[ticker_df['BACKTEST_PL'] > 0])}")
        print(f"Winning Profit: {sum(ticker_df[ticker_df['BACKTEST_PL'] > 0]['BACKTEST_PL'])}")
        print(f"Losing Trades: {len(ticker_df[ticker_df['BACKTEST_PL'] < 0])}")
        print(f"Losing Losses: {sum(ticker_df[ticker_df['BACKTEST_PL'] < 0]['BACKTEST_PL'])}")
        print(f"Max Profit: {max(ticker_df['BACKTEST_PL'])}")
        print(f"Max Loss: {min(ticker_df['BACKTEST_PL'])}")
        return ticker_df
