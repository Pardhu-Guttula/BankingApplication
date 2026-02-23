# Epic Title: Store Order Information in PostgreSQL Database

from sqlalchemy.orm import Session
from backend.orders.repositories.order_repository import OrderRepository

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create_order(self, db: Session, order_id: str, user_id: int, total_amount: float, transaction_id: str, items: list):
        order = self.order_repository.create_order(order_id, user_id, total_amount, transaction_id)
        for item in items:
            self.order_repository.add_order_item(order.id, item['product_id'], item['quantity'], item['price'])
        return order