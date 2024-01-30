from pydantic import BaseModel


class Product(BaseModel):
    name: str
    selling_price: int
    purchase_price: int
    stock: int