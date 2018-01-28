from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from .Base import Base

merchant_on_market = Table('merchant_on_market', Base.metadata,
    Column('merchant_id', Integer, ForeignKey('merchants.id')),
    Column('marketplace_id', Integer, ForeignKey('marketplaces.id')))

class MarketPlace(Base):
    __tablename__ = 'marketplaces'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    merchants = relationship('Merchant', secondary=merchant_on_market,
        back_populates='marketplaces')

class Merchant(Base):
    __tablename__ = 'merchants'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    marketplaces = relationship('MarketPlace', secondary=merchant_on_market,
        back_populates='merchants')
