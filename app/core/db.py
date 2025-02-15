from sqlalchemy import create_engine #type: ignore
from sqlalchemy.ext.declarative import declarative_base #type: ignore
from sqlalchemy.orm import sessionmaker #type: ignore
from dotenv import load_dotenv #type:ignore
from core.config import DATABASE_URL
import os

load_dotenv()


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
