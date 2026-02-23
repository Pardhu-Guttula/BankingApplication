# Epic Title: Create Orders Table in PostgreSQL

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.orders.repositories.order_repository import OrderRepository
from backend.orders.services.order_service import OrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/add', methods=['POST'])
def add_order():
    db = next(get_db())
    order_repository = OrderRepository(db)
    order_service = OrderService(order_repository)

    try:
        data = request.get_json()

        user_id = data['user_id']
        total_amount = data['total_amount']

        new_order = order_service.add_order(db, user_id, total_amount)
        return jsonify({"message": "Order added successfully"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except SQLAlchemyError as se:
        return jsonify({"error": "Database error occurred"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400