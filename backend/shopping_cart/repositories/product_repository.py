# Epic Title: Update product quantities in the shopping cart

from backend.shopping_cart.models.product import Product
from typing import List, Optional
import mysql.connector

class ProductRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT id, name, price, description, available FROM products WHERE id = %s", (product_id,))
            result = cursor.fetchone()
            if result:
                return Product(*result)
            else:
                return None
        finally:
            cursor.close()
            connection.close()

    def get_product_available_quantity(self, product_id: int) -> Optional[int]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT available FROM products WHERE id = %s", (product_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        finally:
            cursor.close()
            connection.close()