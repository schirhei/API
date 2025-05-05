from pydantic import BaseModel

class Order(BaseModel):
    name: str
    creditCard: int
    product: str