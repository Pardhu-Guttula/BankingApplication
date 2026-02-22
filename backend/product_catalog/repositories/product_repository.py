# Epic Title: Sort Products by Price

from backend.product_catalog.models.product import Product
from typing import List
import mysql.connector

class ProductRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_products_sorted_by_price(self, order: str) -> List<Product]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute(f"SELECT id, name, price, description FROM products ORDER BY price {order}")
            results = cursor.fetchall()
            return [Product(id=row[0], name=row[1], price=row[2], description=row[3]) for row in results]
        finally:
            cursor.close()
            connection.close()