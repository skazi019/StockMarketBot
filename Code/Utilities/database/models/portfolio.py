from sqlalchemy import Column, String, Integer, Float, TIMESTAMP
from sqlalchemy.orm import relationship, backref

from Code.Utilities.database.db_util import DatabaseUtil

driver = DatabaseUtil()
session, base = driver._get_session_and_base()


class Portfolio:
    __tablename__ = 'portfolio'

    id = Column(Integer, autoincrement=True)
    name = Column(String)
    date_of_purchase = Column(TIMESTAMP)
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
