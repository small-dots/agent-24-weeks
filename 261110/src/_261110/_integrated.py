# 综合实战

# .env 读取 API 地址和超时时间。
# 一个 AsyncClient 复用 HTTP 连接。
# asyncio.gather 并发请求 3 个用户。
# 按超时、HTTP 状态码、网络错误分别返回规范结果。
# 这是下一步做 Agent Tool Calling 的基础

import os 
import asyncio

import httpx
from dotenv import load_dotenv

load_dotenv()


clinet = httpx.AsyncClient(timeout=10.0)
base_url = os.getenv("API_BASE_URL","")

async def get_user(id:str):
  res = await clinet.get(base_url+f"/users/{id}")
  return res.json()



async def main():
  ress =  await asyncio.gather(get_user(1),get_user(2),get_user(3))
  print(ress)

asyncio.run(main())
