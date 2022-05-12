"""Run once to create a db table(s)"""
from database import Base, engine
from models import Item

print("Creating Database...")

Base.metadata.create_all(engine)