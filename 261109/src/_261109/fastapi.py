from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI(title ="Agent API", description="Agent API for testing", version="0.1.0")

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None
    count: int = Field(..., ge=0, le=120, description="数量")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}
