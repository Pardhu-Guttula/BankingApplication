# Epic Title: Update product quantities in the shopping cart

from backend.shopping_cart.models.shopping_cart import ShoppingCart
from backend.shopping_cart.models.cart_item import CartItem
from backend.user_profile.models.user import User
from typing import Optional
import mysql.connector

class ShoppingCartRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_cart_by_user_id(self, user_id: int) -> Optional[ShoppingCart]:
        connection = mysql.connector.connect(**self.db_config)
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

    def update_item_quantity(self, user_id: int, product_id: int, quantity: int) -> bool:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            # Fetch available product quantity
            cursor.execute("SELECT available FROM products WHERE id = %s", (product_id,))
            available_quantity = cursor.fetchone()[0]
            
            if quantity > available_quantity:
                return False

            if quantity == 0:
                cursor.execute("DELETE FROM cart_items WHERE cart_user_id = %s AND product_id = %s", (user_id, product_id))
            else:
                cursor.execute("UPDATE cart_items SET quantity = %s WHERE cart_user_id = %s AND product_id = %s", (quantity, user_id, product_id))
            
            connection.commit()
            return True
        finally:
            cursor.close()
            connection.close()