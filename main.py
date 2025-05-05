from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import sqlite3

from models.order import Order
from controllers.SQL_commands import run_SQL_command


app = FastAPI()


@app.get("/")
async def get_hello_world():
    return {"Message": "Hello World"}


@app.get("/time")
async def get_time():
    return {"Time": datetime.now()}


@app.get("/order/{order_id}")
async def get_order(order_id: int):
    crsr = run_SQL_command('payment.db', f"""SELECT * FROM Checkout WHERE rowid = {order_id}""")
    order = crsr.fetchall()
    return {"Order": order}


@app.post("/checkout")
async def checkout_order(order: Order):
    try:
        crsr = run_SQL_command('payment.db', f"""INSERT INTO Checkout VALUES ("{order.name}", {order.creditCard}, "{order.product}");""")
        order_id = crsr.lastrowid
    except sqlite3.OperationalError as e:
        raise HTTPException(status_code=500, detail="Database error")
    return {"Order ID": order_id}