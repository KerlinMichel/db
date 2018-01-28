from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from .Base import Base

class Product(Base):
    __tablename__ = 'products'

    upc = Column(String, primary_key=True)
    name = Column(String)
    pricehistory = relationship('ProductPriceHistory')

class ProductPriceHistory(Base):
    __tablename__ = 'productpricehistories'

    id = Column(Integer, primary_key=True)
    item_upc = Column(String, ForeignKey('products.upc'))
    price = Column(String)
    date = Column(Date)
    merchant = Column(String)
