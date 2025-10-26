# category_schemas.py
from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    name: str
    sort_order: Optional[int] = 0
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
