# Epic Title: Manage and Update Order Statuses

from sqlalchemy.orm import Session
from backend.order_management.models.order import Order

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, order_id: str, user_id: int, total_amount: float, transaction_id: str, status: str) -> Order:
        order = Order(
            order_id=order_id,
            user_id=user_id,
            total_amount=total_amount,
            transaction_id=transaction_id,
            status=status,
        )
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def get_order_by_id(self, order_id: str) -> Order:
        return self.db.query(Order).filter(Order.order_id == order_id).first()

    def update_order_status(self, order_id: str, new_status: str) -> Order:
        order = self.get_order_by_id(order_id)
        if order:
            order.status = new_status
            self.db.commit()
            self.db.refresh(order)
        return order