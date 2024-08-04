from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from src.util.base import Base
from datetime import datetime
import uuid


class User(AsyncAttrs, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    personal_id = Column(String, unique=True, default=lambda: str(uuid.uuid4()), index=True)
    full_name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
    registered_at = Column(DateTime, default=datetime.utcnow)
    links = relationship("Link", back_populates="user")


#     password_auth = relationship('PasswordAuth', uselist=False, back_populates='user')
#     sso_auth = relationship('SSOAuth', uselist=False, back_populates='user')
#
#
# class PasswordAuth(Base):
#     __tablename__ = 'password_auth'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     password_hash = Column(String(128), nullable=False)
#     user = relationship('User', back_populates='password_auth')
#
#
# class SSOAuth(Base):
#     __tablename__ = 'sso_auth'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     provider = Column(String(50), nullable=False)
#     provider_user_id = Column(String(100), nullable=False, unique=True)
#     user = relationship('User', back_populates='sso_auth')

class Link(AsyncAttrs, Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    users = relationship("User", back_populates="links")
