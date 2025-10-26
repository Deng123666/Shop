from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from schemas.user_schema import UserCreate, UserResponse
from crud.user_crud import get_user, get_users, create_user
from fastapi import Depends, APIRouter, HTTPException

# 创建路由
user_app = APIRouter()

# 初始化数据库
init_db()

# 依赖项
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_app.post("/")
async def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.dict())

@user_app.get("/", response_model=list[UserResponse])
async def read_users(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    users = get_users(db, page=page, page_size=page_size)
    return users

@user_app.get("/{id}", response_model=UserResponse)
async def read_user(id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
