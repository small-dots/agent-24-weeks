# 本地开发 时可以使用 python-dotenv
# .env:
# API_BASE_URL=https://jsonplaceholder.typicode.com
# HTTP_TIMEOUT = 10


import os 
from dotenv import load_dotenv
load_dotenv()


base_url = os.getenv("API_BASE_URL","")
timeout = float(os.getenv("HTTP_TIMEOUT","10"))


print(base_url)
print(timeout)
# 环境变量读到的是字符串，数值参数要转换类型。
# load_dotenv() 默认不覆盖进程中已经存在的同名环境变量。
# .env 一定要加入 .gitignore，只提交 .env.example。
# 生产环境推荐从部署平台注入环境变量；不要把密钥打印到日志。
