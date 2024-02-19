from app.db.product_repository import ProductRepository
from app.models import Product

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def create_product(self, product: Product):
        return self.repo.add_product(product)

    def get_product(self, id: int):
        return self.repo.get_product(id)
