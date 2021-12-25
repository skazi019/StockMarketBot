
class TechnicalIndicators:

    def __init__(self):
        pass

    @staticmethod
    async def calculate_all_emas(ticker_df):
        emas = [9, 21]#, 50, 200]
        for ma in emas:
            ticker_df[f'{ma}_EMA'] = ticker_df.loc[:, 'Close'].ewm(span=ma, adjust=False).mean()
        return ticker_df
