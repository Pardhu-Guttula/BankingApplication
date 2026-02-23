# Epic Title: Store Order Information in PostgreSQL Database

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.orders.repositories.order_repository import OrderRepository
from backend.orders.services.order_service import OrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/order/create', methods=['POST'])
def create_order():
    db = next(get_db())
    data = request.get_json()
    order_id = data.get('order_id')
    user_id = data.get('user_id')
    total_amount = data.get('total_amount')
    transaction_id = data.get('transaction_id')
    items = data.get('items')

    order_repository = OrderRepository(db)
    order_service = OrderService(order_repository)

    try:
        order = order_service.create_order(db, order_id, user_id, total_amount, transaction_id, items)
        return jsonify({
            "order_id": order.order_id,
            "user_id": order.user_id,
            "total_amount": order.total_amount,
            "transaction_id": order.transaction_id,
            "created_at": order.created_at
        }), 201
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400