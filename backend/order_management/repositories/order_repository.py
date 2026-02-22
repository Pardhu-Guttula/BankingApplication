# Epic Title: Manage and Update Order Statuses

from backend.order_management.models.order import Order, OrderItem, OrderStatus
from typing import Optional, List
import mysql.connector

class OrderRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT order_id, user_id, total_amount, status FROM orders WHERE order_id = %s", (order_id,))
            order_result = cursor.fetchone()
            
            if order_result:
                cursor.execute("SELECT item_id, name, price, quantity FROM order_items WHERE order_id = %s", (order_id,))
                items_results = cursor.fetchall()
                
                items = [OrderItem(id=row[0], name=row[1], price=row[2], quantity=row[3]) for row in items_results]
                return Order(order_id=order_result[0], user_id=order_result[1], items=items, total_amount=order_result[2], status=order_result[3])
            else:
                return None
        finally:
            cursor.close()
            connection.close()

    def update_order_status(self, order_status: OrderStatus) -> bool:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                UPDATE orders SET status = %s WHERE order_id = %s
            """, (order_status.status, order_status.order_id))
            
            cursor.execute("""
                INSERT INTO order_status_updates (order_id, status, updated_at, updated_by)
                VALUES (%s, %s, %s, %s)
            """, (order_status.order_id, order_status.status, order_status.updated_at, order_status.updated_by))
            
            connection.commit()
            return True
        finally:
            cursor.close()
            connection.close()