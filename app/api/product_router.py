from fastapi import APIRouter, Depends, HTTPException
from app.core.product_service import ProductService
from app.db.database import get_db
from app.models import Product

router = APIRouter()

@router.post("/products/", response_model=Product)
def create_product(product: Product, service: ProductService = Depends()):
    return service.create_product(product)

@router.get("/products/{id}", response_model=Product)
def read_product(id: int, service: ProductService = Depends()):
    product = service.get_product(id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
