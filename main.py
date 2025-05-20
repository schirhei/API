from fastapi import FastAPI
from datetime import datetime
from controllers.order_controller import get_order_by_id, process_checkout_order
from models.order import Order

app = FastAPI()


@app.get("/")
async def get_hello_world():
    return {"Message": "Hello World"}


@app.get("/time")
async def get_time():
    return {"Time": datetime.now()}


@app.get("/order/{order_id}")
async def get_order(order_id: int):
    order = get_order_by_id(order_id)
    return {"Order": order}


@app.post("/checkout")
async def checkout_order(order: Order):
    order_id = process_checkout_order(order)
    return {"Order ID": order_id}