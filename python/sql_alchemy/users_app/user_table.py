import datetime as dt
import os
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, create_engine

Base = declarative_base()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'site.db')
# create n connect to db
engine = create_engine(connection_string, echo=True)

Session = sessionmaker()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), unique=True, nullable=False)
    date_created = Column(DateTime(), default=dt.datetime.utcnow)

    def __str__(self):
        return f"User username={self.username}"


