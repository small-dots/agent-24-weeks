from typing import Literal,TypedDict
name: str = "string"

age: int = 25

score: float = 99.5

active: bool = True

names: list[str] = ["Alice", "Bob", "Charlie"]

scores: dict[str, int] = {"Alice": 90}

tags :set[str] = {"python", "typing", "code"}

user: tuple[str, int] = ("Alice", 30)

# 联合类型
user_id:int | str = "12345"

nickname:str | None = None

# 函数参数以及返回

def add(a:int,b:int) ->int:
    return a + b

def greet(name:str) -> str:
    return f"Hello, {name}!"

def print_message(message:str) -> None:
    print(message)

def find_user(user_id:int) -> dict[str,str] | None:
    if(user_id==1):
      return {"name":"Alice"}
    return None

# Literal 限制为指定值
role = Literal["admin", "user", "guest"] 
def get_role(role: role) -> str:
    return f"Role is {role}"

class AgentState(TypedDict):
    messages:list[str]
    status:Literal["idle","runing","done"]
    retry_count:int


def execute_agent(state:AgentState)-> AgentState:
    state["status"] = "running"
    state["messages"].append("Agent started")
    state["status"] = "done"
    state["retry_count"] += 1
    return state


print(name)
print(age)
print(score)
print(active)
print(names)
print(scores)
print(tags)
print(user)
print(user_id)
print(nickname)
print(add(5, 10))
print(greet("Alice"))
print_message("This is a test message.")
print(find_user(1))
print (find_user(2))
print(get_role("dassd"))

print(execute_agent({"messages": [], "status": "idle", "retry_count": 0}))
