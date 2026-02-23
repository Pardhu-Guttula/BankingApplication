# Epic Title: Manage and Update Order Statuses

from sqlalchemy.orm import Session
from backend.order_management.repositories.order_repository import OrderRepository

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def update_order_status(self, db: Session, order_id: str, new_status: str):
        order = self.order_repository.update_order_status(order_id, new_status)
        return order