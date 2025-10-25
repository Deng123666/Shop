# main.py
from fastapi import FastAPI

from routers import user_router
from routers.product_router import product_app
from routers.user_router import user_app



app = FastAPI()

app.include_router(product_app, prefix="/products", tags=["商品"])
app.include_router(user_app, prefix="/users", tags=["用户"])
