# Epic Title: Display order confirmation to customers after successful payment

from backend.order_management.models.order import Order, OrderItem
from typing import Optional, List
import mysql.connector

class OrderRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def save_order(self, order: Order) -> bool:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO orders (order_id, transaction_id, total_amount, customer_email)
                VALUES (%s, %s, %s, %s)
            """, (order.order_id, order.transaction_id, order.total_amount, order.customer_email))
            
            for item in order.items:
                cursor.execute("""
                    INSERT INTO order_items (order_id, item_id, name, price, quantity)
                    VALUES (%s, %s, %s, %s, %s)
                """, (order.order_id, item.id, item.name, item.price, item.quantity))
                
            connection.commit()
            return True
        finally:
            cursor.close()
            connection.close()
    
    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT order_id, transaction_id, total_amount, customer_email FROM orders WHERE order_id = %s", (order_id,))
            order_result = cursor.fetchone()
            
            if order_result:
                cursor.execute("SELECT item_id, name, price, quantity FROM order_items WHERE order_id = %s", (order_id,))
                items_results = cursor.fetchall()
                
                items = [OrderItem(id=row[0], name=row[1], price=row[2], quantity=row[3]) for row in items_results]
                return Order(order_id=order_result[0], transaction_id=order_result[1], items=items, total_amount=order_result[2], customer_email=order_result[3])
            else:
                return None
        finally:
            cursor.close()
            connection.close()