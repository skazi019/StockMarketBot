from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, TIMESTAMP, Sequence

from Code.Utilities.database.db_util import DatabaseUtil

driver = DatabaseUtil()
session, base = driver._get_session_and_base()


class TradeBook:
    __tablename__ = 'tradebook'

    id = Column(Sequence, primary_key=True, )
    name = Column(String)
    date_of_purchase = Column(TIMESTAMP, default=datetime.now())
    qty = Column(Integer)
    price = Column(Float)
    invested = Column(Float)
    algorithm_used = Column(String)

    def __init__(self, name, date_of_purchase, qty, price, invested, algorithm_used):
        self.name = name
        self.date_of_purchase = date_of_purchase
        self.qty = qty
        self.price = price
        self.invested = invested
        self.algorithm_used = algorithm_used
