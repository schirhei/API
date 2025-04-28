from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import csv
import sqlite3

app = FastAPI()

class Order(BaseModel):
    name: str
    creditCard: int
    product: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello():
    return {"message": datetime.now()}


@app.get("/create", status_code=200)
async def create():
    try:
        with sqlite3.connect('payment.db') as conn:
            crsr = conn.cursor()
            crsr.execute("CREATE TABLE checkout (Name TEXT, CreditCard INTEGER, Product TEXT)")
            conn.commit()
    except sqlite3.OperationalError as e:
        print(e)
        raise HTTPException(status_code=500, detail="Database error")
    return {"ok":True}


@app.post("/checkout", status_code=200)
async def checkout(order: Order):
    ans = []
    try:
        with sqlite3.connect('payment.db') as conn:
            crsr = conn.cursor()
            crsr.execute(f"""INSERT INTO checkout VALUES ("{order.name}", {order.creditCard}, "{order.product}");""")
            conn.commit()

            # for debugging
            crsr.execute("SELECT * FROM checkout")
            ans = crsr.fetchall()
            for i in ans:
                print(i)
    except sqlite3.OperationalError as e:
        print(e)
        raise HTTPException(status_code=500, detail="Database error")
    
    return {"ok": ans}