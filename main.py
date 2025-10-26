# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import init_db
from routers import user_router
from routers.product_router import product_app
from routers.user_router import user_app
from routers.category_router import category_app



app = FastAPI(title="Shop", description="Shop API")

app.include_router(product_app, prefix="/products", tags=["商品"])
app.include_router(user_app, prefix="/users", tags=["用户"])
app.include_router(category_app, prefix="/categories", tags=["分类"])

@app.get("/")
def read_root():
    return {"message": "Shop API is running"}

@app.get("/health")
def health_check(db: Session = Depends(init_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}