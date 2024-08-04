from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from src.config.settings import settings
from src.util.base import Base
from datetime import datetime
from nanoid import generate


class User(AsyncAttrs, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    personal_id = Column(String(100), unique=True, default=lambda: str(generate(size=settings.NANOID_STRING_SIZE)),
                         index=True)
    profile_picture = Column(String, nullable=True)
    full_name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    role = Column(String, default="user")
    registered_at = Column(DateTime, default=datetime.utcnow)
    qr_code = Column(String, nullable=True)
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
