"""
author: Kaushal Sharma
date: 2021-11-05
This file fetches data for the specified scrip from the exchange
"""

from Code.Utilities.config.config_util import ConfigUtil


class FetchData:

    __config = ConfigUtil._get_config('stockmarket')
    __querystring = {"datatype": "json"}

    __headers = {
        'x-rapidapi-host': __config['alphavanage']['host'],
        'x-rapidapi-key': __config['alphavanage']['api-key']
    }

    @classmethod
    def _fetch_data(cls, scrip='BANKNIFTY', timeframe='5m'):

        pass


FetchData()