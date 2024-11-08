# 先下载一个可以运行 Flask 的基础镜像
FROM python:3.10

# 设置作者信息
LABEL maintainer="rice"

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到 Docker 引擎中的工作目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露端口
EXPOSE 5001

# 执行我们的脚本文件
CMD ["python3", "news.py", "0.0.0.0", "5001"]
