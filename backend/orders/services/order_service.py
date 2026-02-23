# Epic Title: Create Orders Table in PostgreSQL

from sqlalchemy.orm import Session
from backend.orders.repositories.order_repository import OrderRepository
from backend.orders.models.order import Order

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def add_order(self, db: Session, user_id: int, total_amount: float) -> Order:
        if total_amount <= 0:
            raise ValueError("Total amount must be a positive value")

        new_order = self.order_repository.create_order(user_id, total_amount)
        return new_order