# Epic Title: Filter Products by Category

from backend.product_catalog.models.product import Product
from typing import List, Optional
import mysql.connector

class ProductRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_products_by_category(self, category_id: int) -> List[Product]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT id, name, price, description FROM products WHERE category_id = %s", (category_id,))
            results = cursor.fetchall()
            return [Product(id=row[0], name=row[1], price=row[2], description=row[3]) for row in results]
        finally:
            cursor.close()
            connection.close()