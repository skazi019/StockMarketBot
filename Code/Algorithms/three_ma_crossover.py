import numpy as np


class ThreeMaCrossover:

    def __init__(self):
        pass

    @staticmethod
    async def identify_crossovers(ticker_df):
        ticker_df['SIGNAL'] = ''
        # ticker_df['CLOSE_9_CROSS'] = np.where(ticker_df['Close'] > ticker_df['9_EMA'], 1.0, 0.0)
        # ticker_df['CLOSE_9_CROSS'] = ticker_df['CLOSE_9_CROSS'].diff()
        # ticker_df['SIGNAL'] = ticker_df.apply(
        #     lambda x: 'BUY' if x['CLOSE_9_CROSS'] == 1 else x['SIGNAL']
        # , axis=1)

        ticker_df['9_21_CROSS'] = np.where(ticker_df['9_EMA'] > ticker_df['21_EMA'], 1.0, 0.0)
        ticker_df['9_21_CROSS'] = ticker_df['9_21_CROSS'].diff()
        ticker_df['SIGNAL'] = ticker_df.apply(
            lambda x: 'BUY' if x['9_21_CROSS'] == -1 else 'SELL' if x['9_21_CROSS'] == 1 else x['SIGNAL']
        , axis=1)

        ticker_df['SIGNAL'].fillna(0, inplace=True)

        return ticker_df