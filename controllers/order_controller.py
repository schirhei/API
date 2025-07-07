from models.order import Order
from database.sql_utils import insert_order, get_order

def process_checkout_order(order: Order, db: str):
    # perform preprocessing such as validating the order model data and the user

    # then, database function 
    order_id = insert_order(order, db)
    return order_id

def get_order_by_id(order_id: int, db: str):
    # perform preprocessing such as validating the order model data and the user

    # then, database function
    order = get_order(order_id, db)
    return order