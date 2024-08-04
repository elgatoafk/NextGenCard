from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    personal_id: str
    profile_picture: Optional[str] = None
    full_name: Optional[str] = None
    bio: Optional[str] = None
    role: Optional[str] = "user"
    registered_at: datetime
    qr_code: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    links: List['Link'] = []

    class Config:
        orm_mode = True


class PasswordAuthBase(BaseModel):
    user_id: int
    password_hash: str


class PasswordAuthCreate(PasswordAuthBase):
    pass


class PasswordAuth(PasswordAuthBase):
    id: int

    class Config:
        orm_mode = True


class SSOAuthBase(BaseModel):
    user_id: int
    provider: str
    provider_user_id: str


class SSOAuthCreate(SSOAuthBase):
    pass


class SSOAuth(SSOAuthBase):
    id: int

    class Config:
        orm_mode = True


class LinkBase(BaseModel):
    user_id: int
    url: HttpUrl
    description: Optional[str] = None


class LinkCreate(LinkBase):
    pass


class Link(LinkBase):
    id: int

    class Config:
        orm_mode = True
