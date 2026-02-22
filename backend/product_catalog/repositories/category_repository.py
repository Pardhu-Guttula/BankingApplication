# Epic Title: Filter Products by Category

from backend.product_catalog.models.category import Category
from typing import List, Optional
import mysql.connector

class CategoryRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_all_categories(self) -> List[Category]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT id, name FROM categories")
            results = cursor.fetchall()
            return [Category(id=row[0], name=row[1]) for row in results]
        finally:
            cursor.close()
            connection.close()