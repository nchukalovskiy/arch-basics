from pydantic import BaseModel

#jsonschema - более легковесный, но менее удобный
class Product(BaseModel):
    id: int
    name: str
    price: float
