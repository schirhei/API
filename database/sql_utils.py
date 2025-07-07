import sqlite3
from models.order import Order

def execute_SQL_command(database, command):
    with sqlite3.connect(database) as conn:
        crsr = conn.cursor()
        crsr.execute(command)
        conn.commit()
    return crsr

def get_order(id: int, db: str) -> Order:
    crsr = execute_SQL_command(db, f"""SELECT * FROM Checkout WHERE rowid = {id}""")
    order = crsr.fetchall()
    return order

def insert_order(order: Order, db: str) -> int:
    crsr = execute_SQL_command(db, f"""INSERT INTO Checkout VALUES ("{order.name}", {order.creditCard}, "{order.product}");""")
    order_id = crsr.lastrowid
    return order_id