# Epic Title: View Order History

from sqlalchemy.orm import Session
from backend.order_management.repositories.order_repository import OrderRepository

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def view_order_history(self, db: Session, user_id: int):
        orders = self.order_repository.get_orders_by_user_id(user_id)
        if orders:
            return [{
                "order_id": order.order_id,
                "items": [{
                    "product_id": item.product_id,
                    "quantity": item.quantity,
                    "price": item.price
                } for item in order.items],
                "total_amount": order.total_amount,
                "status": order.status,
                "created_at": order.created_at
            } for order in orders]
        return []