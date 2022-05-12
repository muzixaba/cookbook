from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
# from .python import postgres_password
from sqlalchemy.orm import sessionmaker
# engine = create_engine("sqlite:///test.db")

# db creds
user = "postgres"
pword = "Eyamile"

engine = create_engine(
    f"postgresql://{user}:{pword}@localhost/item_db",
    echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

