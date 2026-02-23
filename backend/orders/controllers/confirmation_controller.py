# Epic Title: Display Order Confirmation to Customers After Successful Payment

from flask import Blueprint, request, render_template, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.orders.repositories.order_repository import OrderRepository
from backend.orders.repositories.transaction_repository import TransactionRepository
from backend.email_service import send_confirmation_email

confirmation_bp = Blueprint('confirmation', __name__)

@confirmation_bp.route('/order/confirmation', methods=['GET'])
def display_order_confirmation():
    db = next(get_db())
    order_id = request.args.get('order_id')

    order_repository = OrderRepository(db)
    transaction_repository = TransactionRepository(db)

    try:
        order = order_repository.get_order_by_id(order_id)
        transaction = transaction_repository.get_transaction_by_id(order.transaction_id)

        if order and transaction:
            order_details = {
                "order_id": order.order_id,
                "user_id": order.user_id,
                "total_amount": order.total_amount,
                "transaction_id": order.transaction_id,
                "created_at": order.created_at,
                "items": [{
                    "product_id": item.product_id,
                    "quantity": item.quantity,
                    "price": item.price
                } for item in order.items]
            }
            send_confirmation_email(order.user_id, order_details)
            return render_template('confirmation.html', order_details=order_details)
        return jsonify({"error": "Order not found"}), 404
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500