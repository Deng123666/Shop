# product_crud.py
from sqlalchemy.orm import Session
from models.Product import Product


def create_product(db: Session, product: dict):
    db_product = Product(**product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()


def get_user_products(db: Session, user_id: int):
    return db.query(Product).filter(Product.owner_id == user_id).all()


def update_product(db: Session, product_id: int, product: dict):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        for key, value in product.items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return True
    return False
