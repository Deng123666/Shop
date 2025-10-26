# category_crud.py
from sqlalchemy.orm import Session
from models.Category import Category
from schemas.category_schemas import CategoryCreate, CategoryUpdate


# 创建分类
def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# 获取分类
def get_category(db: Session, category_id: int):
    """
    用途: 根据 category_id 获取单个分类
    查询方式: 使用 filter 精确匹配 Category.id
    返回值: 返回单个 Category 对象或 None
    """
    return db.query(Category).filter(Category.id == category_id).first()


# 直接获取所有分类
def get_categories(db: Session, page:int = 1, page_size:int = 10):
    """
    用途: 获取分类列表，支持分页
    查询方式: 使用 offset 和 limit 实现分页查询
    返回值: 返回 Category 对象列表
    """
    skip = (page - 1) * page_size
    categories = db.query(Category).offset(skip).limit(page_size).all()

    return categories


# # 按sort_order和name排序获取分类
# def get_categories_with_sort(db: Session):
#     """
#     用途: 获取所有分类并按指定规则排序
#     查询方式: 使用 order_by 按 sort_order 和 name 排序
#     返回值: 返回排序后的 Category 对象列表
#     """
#     return db.query(Category).order_by(Category.sort_order, Category.name).all()


# 更新分类
def update_category(db: Session, category_id: int, category: CategoryUpdate):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        update_data = category.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
    return db_category


# 删除分类
def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False
