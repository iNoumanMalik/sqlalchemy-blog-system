from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///blog.db"

class Base(DeclarativeBase):
    pass

engine = create_engine(DATABASE_URL, echo=True) #Connects to the database

session = sessionmaker(bind=engine, autoflush=False, autocommit=False) #Talks to the database

#echo=True → see generated SQL
#autoflush=False → safer for multi-step inserts
#autocommit=False → commits only when you call session.commit()