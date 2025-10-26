from pydantic import BaseModel, EmailStr
from typing import List, Optional
from schemas.product_schemas import Product


class UserCreate(BaseModel):
    tel: str
    password: str


class UserUpdate(UserCreate):
    email: Optional[str] = None
    nickname: Optional[str] = None
    address: Optional[str] = None
    avatar_url: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    tel: str
    email: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    tel: str
    password: str

# 密码重置模型
class PasswordReset(BaseModel):
    new_password: str

