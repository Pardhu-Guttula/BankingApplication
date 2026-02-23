# Epic Title: View Order History

from sqlalchemy.orm import Session
from backend.order_management.models.order import Order
from backend.order_management.models.order_item import OrderItem

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

    def add_order_item(self, order_id: int, product_id: int, quantity: int, price: float):
        order_item = OrderItem(
            order_id=order_id,
            product_id=product_id,
            quantity=quantity,
            price=price,
        )
        self.db.add(order_item)
        self.db.commit()
        self.db.refresh(order_item)
        return order_item

    def get_order_by_id(self, order_id: int) -> Order:
        return self.db.query(Order).filter(Order.id == order_id).first()

    def get_orders_by_user_id(self, user_id: int):
        return self.db.query(Order).filter(Order.user_id == user_id).order_by(Order.created_at.desc()).all()