from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .Base import Base

class Product(Base):
    __tablename__ = 'products'

    upc = Column(String, primary_key=True)
    name = Column(String)
    last_updated = Column(DateTime, onupdate=datetime.now)
    pricehistory = relationship('ProductPriceHistory')

class ProductPriceHistory(Base):
    __tablename__ = 'productpricehistories'

    id = Column(Integer, primary_key=True)
    item_upc = Column(String, ForeignKey('products.upc'))
    price = Column(String)
    date = Column(Date)
    merchant = Column(String)
