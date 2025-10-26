from pydantic import BaseModel, EmailStr
from typing import List, Optional
from schemas.product_schemas import Product


class UserCreate(BaseModel):
    tel: str
    password: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    avatar_url: Optional[str] = None


class UserResponse(UserUpdate):
    id: int
    tel: str
    password: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    tel: str
    password: str

# 密码重置模型
class PasswordReset(BaseModel):
    new_password: str

