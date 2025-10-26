import hashlib

from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.User import User

def get_hashed_password(password: str) -> str:
    return password


def create_user(db: Session, user: dict):
    hashed_password = get_hashed_password(user["password"])
    db_user = User(
        tel=user["tel"],
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()

def get_users(db: Session, page: int=1, page_size: int=10):
    # 计算偏移量
    skip = (page - 1) * page_size

    # 查询当前页数据
    users = db.query(User).offset(skip).limit(page_size).all()

    return users

def update_user(db: Session, user_id: int, user:dict):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user
