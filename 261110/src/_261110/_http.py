# 使用httpx 支持系统部和异步API 调用
import io
import asyncio
import random

import httpx
from tqdm import tqdm

headers = {'user-agent': 'my-app/0.0.1'}

def gen():
    total =32*1024*1024
    with tqdm(ascii=True, unit_scale=True, unit='B', unit_divisor=1024, total=total) as bar:
        with io.BytesIO(random.randbytes(total)) as f:
            while data:=f.read(1024):
                yield data
                bar.update(len(data))

async def main():
    async with httpx.AsyncClient(timeout=10.0,headers=headers) as client:
        resp = await client.post("https://jsonplaceholder.typicode.com/posts")
        # HTTP 状态码错误时抛出异常
        resp.raise_for_status()
        print(resp.json())

        
asyncio.run(main())

httpx.post("https://httpbin.org/post", content=gen())






# async with 确保HTTP客户端在使用结束后释放资源
# raise_for_status() 4xx/5xx响应抛出HTTPStatusError，不是所有错误都能只靠json() 发现。
# json=...   POST是将Python字典序列化为JSON对象 
# 注意：复用AsyncClient 不要砸你每次亲故去是都创建新的客户端
