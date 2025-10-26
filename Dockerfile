# 使用官方Python镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 复制环境变量文件（如果需要）
COPY .env .env

# 暴露FastAPI默认端口
EXPOSE 8888

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888", "--reload"]