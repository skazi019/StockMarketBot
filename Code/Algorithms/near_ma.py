
from Code.Utilities.config.config_util import ConfigUtil


class NearMA:

    def __init__(self):
        pass

    @staticmethod
    async def near_200_ema(ticker_df):
        ema = ticker_df.iloc[-1]['200_EMA']
        close = ticker_df.iloc[-1]['Close']
        upper_limit = ema + ema * ConfigUtil.get_config(server='algorithms')['near_200_ema']
        lower_limit = ema - ema * ConfigUtil.get_config(server='algorithms')['near_200_ema']
        if lower_limit <= close <= upper_limit:
            return True, close
        else:
            return False
