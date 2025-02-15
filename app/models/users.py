from sqlalchemy import Column, Integer, String #type: ignore
from core.db import Base 

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String)
    hashedpassword = Column(String)
