import database as _database
import models as _models, schemas as _schemas
import sqlalchemy.orm as _orm


def create_database():
    return _database.Base.metadata.create_all(
        bind=_database.engine
    )

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_email(db: _orm.Session, email: str):
    return db.query(_models.User).filter(_models.User.email==email).first() 


def create_user(db: _orm.Session, user: _schemas.UserCreate):
    fake_hashed_pword = user.password + "thisisnotsafe"
    db_user = _models.User(email=user.email, hashed_password=fake_hashed_pword)
    db.add(db_user)
    db.commit()
    db.refreshed()