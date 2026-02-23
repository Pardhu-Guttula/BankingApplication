# Epic Title: View Order History

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.order_management.repositories.order_repository import OrderRepository
from backend.order_management.services.order_service import OrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders/history', methods=['GET'])
def view_order_history():
    db = next(get_db())
    user_id = request.args.get('user_id')

    order_repository = OrderRepository(db)
    order_service = OrderService(order_repository)

    try:
        order_history = order_service.view_order_history(db, user_id)
        if order_history:
            return jsonify(order_history), 200
        return jsonify({"message": "No orders found"}), 404
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500