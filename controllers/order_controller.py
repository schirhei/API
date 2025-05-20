from models.order import Order
from database.sql_utils import execute_SQL_command

def process_checkout_order(order: Order):
    crsr = execute_SQL_command('payment.db', f"""INSERT INTO Checkout VALUES ("{order.name}", {order.creditCard}, "{order.product}");""")
    order_id = crsr.lastrowid
    return order_id

def get_order_by_id(order_id: int):
    crsr = execute_SQL_command('payment.db', f"""SELECT * FROM Checkout WHERE rowid = {order_id}""")
    order = crsr.fetchall()
    return order