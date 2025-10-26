# User.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    # 必选字段
    id = Column(Integer, primary_key=True, index=True)
    tel = Column(String(20), index=True)
    password = Column(String(100), index=True)

    # 可选字段
    name = Column(String(100), index=True, nullable=True)
    address = Column(String(100), index=True, nullable=True)
    email = Column(String(100), index=True, nullable=True)
    products = relationship("Product", back_populates="owner")
