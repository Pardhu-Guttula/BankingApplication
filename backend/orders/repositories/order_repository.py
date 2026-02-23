# Epic Title: Create Orders Table in PostgreSQL

from sqlalchemy.orm import Session
from backend.orders.models.order import Order
from typing import Optional

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, user_id: int, total_amount: float) -> Order:
        db_order = Order(user_id=user_id, total_amount=total_amount)
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        return self.db.query(Order).filter(Order.id == order_id).first()