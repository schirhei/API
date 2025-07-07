from fastapi import FastAPI
from fastapi.testclient import TestClient
from datetime import datetime
from controllers.order_controller import get_order_by_id, process_checkout_order
from models.order import Order
from config import ENV, NP_DATABASE, PR_DATABASE

app = FastAPI()
test_client = TestClient(app)

if ENV == 'NP':
    db = NP_DATABASE
else:
    db = PR_DATABASE


@app.get("/")
async def get_hello_world():
    return {"Message": "Hello World"}


@app.get("/time")
async def get_time():
    return {"Time": datetime.now()}


@app.get("/order/{order_id}")
async def get_order(order_id: int):
    order = get_order_by_id(order_id, db)
    return {"Order": order}


@app.post("/checkout")
async def checkout_order(order: Order):
    order_id = process_checkout_order(order, db)
    return {"Order ID": order_id}