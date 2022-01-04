import numpy as np


class EmaCrossover:

    def __init__(self):
        pass

    @staticmethod
    async def identify_crossovers_close_9ema(ticker_df):
        ticker_df['SIGNAL'] = ''

        ticker_df['CLOSE_9_CROSS'] = np.where(ticker_df['Close'] > ticker_df['9_EMA'], 1.0, 0.0)
        ticker_df['CLOSE_9_CROSS'] = ticker_df['CLOSE_9_CROSS'].diff()
        ticker_df['SIGNAL'] = ticker_df.apply(
            lambda x: 'BUY' if x['CLOSE_9_CROSS'] == -1 else 'SELL' if x['CLOSE_9_CROSS'] == 1 else x['SIGNAL']
            , axis=1)

        ticker_df.drop(['CLOSE_9_CROSS'], axis=1, inplace=True)

        start = ticker_df[ticker_df['SIGNAL'] == 'BUY'].index[0]
        end = ticker_df[ticker_df['SIGNAL'] == 'SELL'].index[-1]
        ticker_df = ticker_df[start:end + 1]
        ticker_df = ticker_df[(ticker_df['SIGNAL'] == 'BUY') | (ticker_df['SIGNAL'] == 'SELL')]
        ticker_df.reset_index(drop=True, inplace=True)

        return ticker_df

    @staticmethod
    async def identify_9_21_crossover(ticker_df):
        ticker_df['SIGNAL'] = ''

        ticker_df['9_21_CROSS'] = np.where(ticker_df['9_EMA'] > ticker_df['21_EMA'], 1.0, 0.0)
        ticker_df['9_21_CROSS'] = ticker_df['9_21_CROSS'].diff()
        ticker_df['SIGNAL'] = ticker_df.apply(
            lambda x: 'BUY' if x['9_21_CROSS'] == 1 else 'SELL' if x['9_21_CROSS'] == -1 else x['SIGNAL']
            , axis=1)

        ticker_df.drop(['9_21_CROSS'], axis=1, inplace=True)

        # start = ticker_df[ticker_df['SIGNAL'] == 'BUY'].index[0]
        # end = ticker_df[ticker_df['SIGNAL'] == 'SELL'].index[-1]
        # ticker_df = ticker_df[start:end + 1]
        # ticker_df = ticker_df[(ticker_df['SIGNAL'] == 'BUY') | (ticker_df['SIGNAL'] == 'SELL')]
        ticker_df.reset_index(inplace=True)

        return ticker_df

    @staticmethod
    async def identify_21_90_crossover(ticker_df):
        ticker_df['SIGNAL'] = ''

        ticker_df['21_90_CROSS'] = np.where(ticker_df['21_EMA'] > ticker_df['90_EMA'], 1.0, 0.0)
        ticker_df['21_90_CROSS'] = ticker_df['21_90_CROSS'].diff()
        ticker_df['SIGNAL'] = ticker_df.apply(
            lambda x: 'BUY' if x['21_90_CROSS'] == 1 else 'SELL' if x['21_90_CROSS'] == -1 else x['SIGNAL']
            , axis=1)

        ticker_df.drop(['21_90_CROSS'], axis=1, inplace=True)

        # start = ticker_df[ticker_df['SIGNAL'] == 'BUY'].index[0]
        # end = ticker_df[ticker_df['SIGNAL'] == 'SELL'].index[-1]
        # ticker_df = ticker_df[start:end + 1]
        # ticker_df = ticker_df[(ticker_df['SIGNAL'] == 'BUY') | (ticker_df['SIGNAL'] == 'SELL')]
        ticker_df.reset_index(inplace=True)

        return ticker_df
