import os
import sys
from dotenv import load_dotenv
from pyexpat import features

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import engine, Base
from models.User import User
from models.Product import Product
from models.Category import Category


def init_database():
    """初始化数据库，创建所有表"""
    print("开始创建数据库表...")

    # 创建所有表
    Base.metadata.create_all(bind=engine)
    print("数据库表创建成功！")
    print("已创建的表：", list(Base.metadata.tables.keys()))


if __name__ == "__main__":
    load_dotenv()  # 加载环境变量
    init_database()
