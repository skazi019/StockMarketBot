import os
import json
from pathlib import Path


class ConfigUtil:

    __config = None
    __base_path = Path(__file__).parent

    @classmethod
    def _set_config(cls):
        try:
            with open(os.path.join(cls.__base_path, 'development.json'), 'rb') as f:
                cls.__config = json.load(f)
        except Exception as e:
            print(e)

    @classmethod
    def get_config(cls, server='postgres'):
        if cls.__config is not None:
            return cls.__config[server]
        else:
            cls._set_config()
            return cls.__config[server]
