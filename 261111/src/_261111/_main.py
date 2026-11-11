# 实战练习：开发一个 FastAPI 服务，包含健康检查接口、业务接口、参数验证和异常处理。
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr,Field
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI(title ="实战练习",root_path="", description="开发一个 FastAPI 服务，包含健康检查接口、业务接口、参数验证和异常处理。", version="0.1.0")


# 健康检查
@app.get("/health")
async def health_check():
    return {"status": "healthy"}



# 业务接口 
class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="用户名，长度在3到50之间")
    email: EmailStr = Field(...,  description="用户邮箱，必须是有效的邮箱格式")
    age: int = Field(..., ge=0, le=120, description="用户年龄，必须在0到120之间")

@app.post("/users")
async def create_user(user: User):
    # 模拟业务逻辑处理
    return {"message": "用户创建成功", "user": user.dict()}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # 模拟获取用户信息
    if user_id == 1:
        return {"user_id": 1, "username": "Alice", "email": "alice@example.com", "age": 30}

# 异常处理


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

