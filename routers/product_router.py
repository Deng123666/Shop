from sqlalchemy.orm import Session

from crud.category_crud import get_category
from crud.user_crud import get_user
from database import SessionLocal, init_db
from schemas.product_schemas import ProductCreate, Product
from crud.product_crud import get_product, get_products, create_product, update_product, delete_product
from fastapi import Depends, APIRouter, HTTPException


# 创建路由
product_app = APIRouter()


# 初始化数据库
init_db()

# 依赖项
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@product_app.post("/", response_model=Product)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    owner_id = product.owner_id
    category_id = product.category_id
    if not get_user(db, owner_id):
        raise HTTPException(status_code=404, detail="User not found")
    elif not get_category(db, category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    return create_product(db, product.dict())

@product_app.get("/", response_model=list[Product])
def read_products(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    products = get_products(db, page=page, page_size=page_size)
    return products

@product_app.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@product_app.put("/{product_id}", response_model=Product)
def update_product_endpoint(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = update_product(db, product_id, product.dict())
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@product_app.delete("/{product_id}")
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    success = delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}