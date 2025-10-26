# category_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from crud.category_crud import create_category, get_category, get_categories, update_category, \
    delete_category
from schemas.category_schemas import CategoryCreate, CategoryUpdate, Category

# 创建路由
category_app = APIRouter()


# 依赖项
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@category_app.post("/", response_model=Category)
def create_category_endpoint(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)


@category_app.get("/", response_model=List[Category])
def read_categories(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    categories = get_categories(db, page=page, page_size=page_size)
    return categories


# @category_app.get("/sorted", response_model=List[Category])
# def read_categories_sorted(db: Session = Depends(get_db)):
#     categories = get_categories_with_sort(db)
#     return categories


@category_app.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@category_app.put("/{category_id}", response_model=Category)
def update_category_endpoint(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    db_category = update_category(db, category_id, category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@category_app.delete("/{category_id}")
def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    success = delete_category(db, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted"}
