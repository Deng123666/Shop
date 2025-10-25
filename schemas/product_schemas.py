# product_schemas.py
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    description: str | None = None
    category: str | None = None
    owner_id: int  # 修改为 int 类型，与数据库模型一致

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True