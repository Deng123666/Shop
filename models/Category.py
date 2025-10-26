# Category.py
import sys
import os
# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__ = "categories"
    
    # 必选字段
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    
    # 可选字段
    sort_order = Column(Integer, default=0)
    description = Column(String(500), nullable=True)
    
    # 建立一对多关系：一个分类包含多个商品
    products = relationship("Product", back_populates="category_rel")