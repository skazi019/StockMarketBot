from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# custom imports
from Code.Utilities.config.config_util import ConfigUtil


class DatabaseUtil:

    def __init__(self):
        self.__session = None
        self.__engine = None
        self.__base = None

    def _create_session(self):
        engine_url = 'postgresql://{username}:{password}@{host}:{port}/{db_name}'
        db_config = ConfigUtil._get_config('postgres')['stockmarketbot']
        self.__engine = create_engine(engine_url. format(username=db_config['username'],
                                                         password=db_config['password'],
                                                         host=db_config['host'],
                                                         port=db_config['port'],
                                                         db_name=db_config['db_name']))
        self.__session = sessionmaker(bind=self.__engine)
        self.__base = declarative_base()

    def _get_session_and_base(self):
        if self.__session is None or self.__base is None:
            self._create_session()
            return self.__session, self.__base
        else:
            return self.__session, self.__base

    def _close_session(self):
        if self.__session:
            self.__session.close()
            self.__engine.dispose()
