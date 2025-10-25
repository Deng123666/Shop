# Product.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    price = Column(Float)
    description = Column(String(500), nullable=True)
    category = Column(String(50), nullable=True)

    # 添加外键关联到用户
    owner_id = Column(Integer, ForeignKey("users.id"))
    # 建立多对一关系：每个商品属于一个用户
    owner = relationship("User", back_populates="products")