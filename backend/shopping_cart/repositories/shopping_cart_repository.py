# Epic Title: Persist shopping cart state in PostgreSQL

from backend.shopping_cart.models.shopping_cart import ShoppingCart
from backend.shopping_cart.models.cart_item import CartItem
from backend.user_profile.models.user import User
from typing import Optional
import psycopg2

class ShoppingCartRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_cart_by_user_id(self, user_id: int) -> Optional[ShoppingCart]:
        connection = psycopg2.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT user_id FROM shopping_carts WHERE user_id = %s", (user_id,))
            user_result = cursor.fetchone()
            if user_result:
                cursor.execute("""
                    SELECT p.id, p.name, p.price, p.description, p.available, ci.quantity
                    FROM cart_items ci
                    JOIN products p ON ci.product_id = p.id
                    WHERE ci.cart_user_id = %s
                """, (user_id,))
                items_results = cursor.fetchall()
                
                items = [CartItem(Product(id=row[0], name=row[1], price=row[2], description=row[3], available=row[4]), quantity=row[5]) for row in items_results]
                return ShoppingCart(user=User(id=user_result[0]), items=items)
            else:
                return None
        finally:
            cursor.close()
            connection.close()

    def add_or_update_item_in_cart(self, user_id: int, product_id: int, quantity: int) -> bool:
        connection = psycopg2.connect(**self.db_config)
        cursor = connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO cart_items (cart_user_id, product_id, quantity)
                VALUES (%s, %s, %s)
                ON CONFLICT (cart_user_id, product_id)
                DO UPDATE SET quantity = EXCLUDED.quantity
                WHERE cart_items.cart_user_id = %s AND cart_items.product_id = %s
            """, (user_id, product_id, quantity, user_id, product_id))
            connection.commit()
            return True
        finally:
            cursor.close()
            connection.close()

    def remove_item_from_cart(self, user_id: int, product_id: int) -> bool:
        connection = psycopg2.connect(**self.db_config)
        cursor = connection.cursor()

        try:
            cursor.execute("DELETE FROM cart_items WHERE cart_user_id = %s AND product_id = %s", (user_id, product_id))
            if cursor.rowcount == 0:
                return False
            connection.commit()
            return True
        finally:
            cursor.close()
            connection.close()