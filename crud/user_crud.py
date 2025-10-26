import hashlib

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

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()
