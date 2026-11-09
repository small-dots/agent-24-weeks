# Pydantic 是 Python 生态中非常重要的一个数据验证和数据结构定义库

# 定义数据结构
# 严重呢个真实输入数据
# 类型转化和约束校验
# 序列化为JSON
from pydantic import BaseModel,EmailStr,Field

class User (BaseModel):
    id: int = Field(..., description="用户ID")
    name: str = Field(..., min_length=1, max_length=50, description="用户名")
    email: EmailStr = Field(..., description="用户邮箱")
    age: int = Field(..., ge=0, le=120, description="用户年龄")

data = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "age": 120
}
# 自动验证并创建对象
user = User(**data)
print(user)
print(user.age)

# 能够可靠地获取结构化数据
class TravelPlan(BaseModel):
    origin: str
    destination: str
    budget: float = Field(gt=0)
    days: int = Field(gt=0, le=30)

# 模拟大模型返回的数据
llm_response = {
    "origin": "北京",
    "destination": "上海",
    "budget": 5000,
    "days": 3
}
plan = TravelPlan(**llm_response)
print(plan.destination)
print(plan.budget)

# agent项目中的作用场景
# 场景：LLM结构化输出
# 作用：限定大模型输出的数据结构

# 场景：Tool Calling 
# 作用：定义工具参数以及校验规则

# 场景：agent状态管理 
# 作用：定义状态数据结构

# 场景：API接口
# 作用：校验请求和响应数据

# 场景：JSON Schema
# 作用：将模型结构转化为JSON Schema，方便前端和后端进行数据交互和验证

# 场景：数据持久化
# 作用：将对象序列化为JSON
