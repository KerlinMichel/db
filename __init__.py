from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models.Base import Base

url = "postgresql://{}:{}@{}:{}/{}".format(
environ.get("DB_USER_NAME"),
environ.get("DB_PASSWORD"),
environ.get("DB_HOST"),
environ.get("DB_PORT"),
environ.get("DB_NAME")
)

engine = create_engine(url)
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()
