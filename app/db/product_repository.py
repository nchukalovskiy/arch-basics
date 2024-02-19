from app.db.database import get_db
from app.models import Product

class ProductRepository:
    def add_product(self, product: Product):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (id, name, price) VALUES (%s, %s, %s)", 
                       (product.id, product.name, product.price))
        connection.commit()
        cursor.close()

    def get_product(self, id: int):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Product(id=result[0], name=result[1], price=result[2])
        else:
            return None
