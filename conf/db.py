from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

#  read db_name from secrets
dbname_file = os.getenv("POSTGRES_DB_FILE")
with open(dbname_file, "r") as f:
    DB_NAME = f.read().strip()

#  read username from secrets
user_file = os.getenv("POSTGRES_USER_FILE")
with open(user_file, "r") as f:
    DB_USER = f.read().strip()

#  read password from secrets
passwd_file = os.getenv("POSTGRES_PASSWORD_FILE")
with open(passwd_file, "r") as f:
    DB_PASSWORD = f.read().strip()


SQLALCHEMY_DATABASE_URL = (f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@postgres:5432/{DB_NAME}")


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, max_overflow=5)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
