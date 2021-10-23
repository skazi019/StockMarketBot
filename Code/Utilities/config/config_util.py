import os
import json
from pathlib import Path


class ConfigUtil:

    def __init__(self):
        self.__config = None
        self.__base_path = Path(__file__).parent

    def _set_config(self):
        try:
            with open(os.path.join(self.__base_path, 'development.json'), 'rb') as f:
                self.__config = json.load(f)
        except Exception as e:
            print(e)

    def _get_config(self, server='postgres'):
        if self.__config is not None:
            return self.__config[server]
        else:
            self._set_config()
            return self.__config[server]
