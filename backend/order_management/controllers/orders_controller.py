# Epic Title: Store Order Data in PostgreSQL

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.order_management.repositories.order_repository import OrderRepository
from backend.order_management.services.order_service import OrderService

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders/create', methods=['POST'])
def create_order():
    db = next(get_db())
    data = request.get_json()

    order_id = data.get('order_id')
    user_id = data.get('user_id')
    total_amount = data.get('total_amount')
    transaction_id = data.get('transaction_id')
    status = data.get('status')
    items = data.get('items')

    order_repository = OrderRepository(db)
    order_service = OrderService(order_repository)

    try:
        order = order_service.create_order(db, order_id, user_id, total_amount, transaction_id, status, items)
        return jsonify({
            "order_id": order.order_id,
            "user_id": order.user_id,
            "total_amount": order.total_amount,
            "status": order.status,
            "created_at": order.created_at
        }), 201
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400

@order_bp.route('/orders/update', methods=['POST'])
def update_order():
    db = next(get_db())
    data = request.get_json()

    order_id = data.get('order_id')
    total_amount = data.get('total_amount')
    status = data.get('status')

    order_repository = OrderRepository(db)
    order_service = OrderService(order_repository)

    try:
        order = order_service.update_order(db, order_id, total_amount, status)
        if order:
            return jsonify({
                "order_id": order.order_id,
                "total_amount": order.total_amount,
                "status": order.status,
                "updated_at": order.updated_at
            }), 200
        return jsonify({"error": "Order not found"}), 404
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@order_bp.route('/orders/<order_id>', methods=['GET'])
def get_order_details(order_id):
    db = next(get_db())

    order_repository = OrderRepository(db)
    order_service = OrderService(order_repository)

    try:
        order = order_service.get_order_by_id(db, order_id)
        if order:
            order_items = [{
                "product_id": item.product_id,
                "quantity": item.quantity,
                "price": item.price
            } for item in order.items]
            return jsonify({
                "order_id": order.order_id,
                "user_id": order.user_id,
                "total_amount": order.total_amount,
                "status": order.status,
                "created_at": order.created_at,
                "updated_at": order.updated_at,
                "items": order_items
            }), 200
        return jsonify({"error": "Order not found"}), 404
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500