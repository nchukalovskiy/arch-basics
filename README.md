# Интернет магазин
- апи на создание товара
- апи на удаление товара
- апи на создание заказа, оно должно
  - проверить существуют ли переданные товары 
  - посчитать суммарную стоимость заказа

## структура 


*   `main.py`: Entry point for the FastAPI application
*   `models.py`: data models
*   `/api`:  FastAPI routers
    *   `product_router.py`: product-related operations
    *   `order_router.py`: order-related operations
*   `/core`: business logic
    *   `product_service.py`: product management
    *   `order_service.py`: order management
*   `/db`: data access logic
    *   `product_repository.py`: data access methods for products
    *   `order_repository.py`: data access methods for orders

https://github.com/kosvish/FastAPI-Online-Store/blob/main/src/models/user.py