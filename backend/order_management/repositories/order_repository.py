# Epic Title: View Order History

from backend.order_management.models.order import Order, OrderItem
from typing import Optional, List
import mysql.connector

class OrderRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_orders_by_user_id(self, user_id: int) -> List[Order]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT order_id, user_id, total_amount, status
                FROM orders 
                WHERE user_id = %s
                ORDER BY order_id DESC
            """, (user_id,))
            orders_results = cursor.fetchall()
            
            orders = []
            for order_result in orders_results:
                cursor.execute("SELECT item_id, name, price, quantity FROM order_items WHERE order_id = %s", (order_result[0],))
                items_results = cursor.fetchall()
                
                items = [OrderItem(id=row[0], name=row[1], price=row[2], quantity=row[3]) for row in items_results]
                order = Order(order_id=order_result[0], user_id=order_result[1], items=items, total_amount=order_result[2], status=order_result[3])
                orders.append(order)
            return orders
        finally:
            cursor.close()
            connection.close()