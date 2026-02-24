from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    username: str
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None