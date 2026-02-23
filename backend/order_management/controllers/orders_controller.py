# Epic Title: Manage and Update Order Statuses

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.order_management.repositories.order_repository import OrderRepository
from backend.order_management.services.order_service import OrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders/update_status', methods=['POST'])
def update_order_status():
    db = next(get_db())
    data = request.get_json()
    order_id = data.get('order_id')
    new_status = data.get('new_status')
    user_role = data.get('user_role')

    if user_role != "administrator":
        return jsonify({"error": "Permission denied"}), 403

    order_repository = OrderRepository(db)
    order_service = OrderService(order_repository)

    try:
        order = order_service.update_order_status(db, order_id, new_status)
        if order:
            return jsonify({
                "order_id": order.order_id,
                "status": order.status,
                "updated_at": order.updated_at
            }), 200
        return jsonify({"error": "Order not found"}), 404
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500