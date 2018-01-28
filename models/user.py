from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from re import match

from .Base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    hash_pass = Column(String, nullable=False)
    address = Column(String)
    mobile_phone = Column(String)

    @validates('email')
    def validate_email(self, key, emailaddress):
        assert match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', address) != None
        return emailaddress

class Unverified_User(Base):
    __tablename__ = 'unverified_users'

    email = Column(String, primary_key=True)
    hash_pass = Column(String, nullable=False)

    @validates('email')
    def validate_email(self, key, emailaddress):
        assert match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', address) != None
        return emailaddress
