# Epic Title: Store Order Data in PostgreSQL

from sqlalchemy.orm import Session
from backend.order_management.repositories.order_repository import OrderRepository

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def create_order(self, db: Session, order_id: str, user_id: int, total_amount: float, transaction_id: str, status: str, items: list):
        order = self.order_repository.create_order(order_id, user_id, total_amount, transaction_id, status)
        for item in items:
            self.order_repository.add_order_item(order.id, item['product_id'], item['quantity'], item['price'])
        return order

    def update_order(self, db: Session, order_id: str, total_amount: float, status: str):
        order = self.order_repository.update_order(order_id, total_amount, status)
        return order

    def get_order_by_id(self, db: Session, order_id: str):
        order = self.order_repository.get_order_by_id(order_id)
        return order

    def get_all_orders(self, db: Session):
        orders = self.order_repository.get_all_orders()
        return orders