# Py 使用try  except  else finally处理异常。  主动抛出异常用raise。
import httpx
import asyncio

try:
  result = 10/0
except ZeroDivisionError:
  print('除数不能为0')
else:
  print("只有无异常时执行：",result)
finally:
  print("无论是否出现异常均执行")

# 网络请求应该正对性区分

async def main():
    async with httpx.AsyncClient(timeout=10.0) as client:

        try:
          response = await client.post("https://jsonplaceholder.typicode.com/posts")
          # HTTP 状态码错误时抛出异常
          response.raise_for_status()
        except httpx.TimeoutException:
          print("超时")
        except httpx.HTTPStatusError as exc:
          print(exc.response.status_code)
        except httpx.RequestError as exc:
          # print("其他网络错误：", exc)

          print(response.json())

asyncio.run(main())


# TimeoutException 属于RequestError 子类， 更具体的异常应该放在前面，不要无差别铺货所有异常在静默忽略
