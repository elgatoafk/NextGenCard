from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from src.util.base import Base
from datetime import datetime


class User(AsyncAttrs, Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    full_name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
    registered_at = Column(DateTime, default=datetime.utcnow)


