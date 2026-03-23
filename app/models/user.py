from sqlalchemy import Column, Integer, String
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    number = Column(String, unique=True, index=True)
    address = Column(String, nullable=True)
    flattype = Column(String, nullable=False)
    budget = Column(Integer, nullable=True)