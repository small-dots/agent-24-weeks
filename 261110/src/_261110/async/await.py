# python 的async def声明协程函数。调用协程函数只会得到协程对象；需要await 、asyncio.run 或者Task才会执行异步逻辑 

import asyncio 
async def fetch(name,delay):
  await asyncio.sleep(delay)
  return name 

async def main():
  results = await asyncio.gather(fetch("A",1),fetch("B",4))
  print(results)

asyncio.run(main())

async def getinfo(name:str,delay:int):
  await asyncio.sleep(delay)
  return name


async def do():
  res = await asyncio.gather(getinfo("张三",2),getinfo('lisi',1))
  print(res)


asyncio.run(do())
# asyncio.run(main()):脚本最外层的启动入口
# await: 在等待期间把控制权交还时间循环
# asyncio.gather: 并发执行多个协程，并按传入顺序返回结果
# 与js不同，Python调用async def 不会想 JS Promise 一样立即执行函数体
# 适合I/O并发：不能简单等同月多和CPU并行


