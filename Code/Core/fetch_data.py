"""
author: Kaushal Sharma
date: 2021-11-05
This file fetches data for the specified scrip from the exchange
"""

from Code.Utilities.config.config_util import ConfigUtil

import aiohttp


class FetchData:
    __config = ConfigUtil._get_config('stockmarket')
    __querystring = {"datatype": "json"}

    __headers = {
        'x-rapidapi-host': __config['alphavanage']['host'],
        'x-rapidapi-key': __config['alphavanage']['api-key']
    }

    @classmethod
    def _fetch_data(cls, symbol='BANKNIFTY', timeperiod='TIME_SERIES_INTRADAY', interval='5m'):
        cls.__querystring['function'] = timeperiod
        cls.__querystring['symbol'] = symbol
        cls.__querystring['interval'] = interval
        with aiohttp.ClientSession() as session:
            with session.get(cls.__config['alphavantage']['url'],
                             headers=cls.__headers, params=cls.__querystring) as data:
                return data


try:
    data = FetchData._fetch_data(symbol='MSFT', timeperiod='TIME_SERIES_INTRADAY', interval='5m')
except Exception as e:
    print(e)
