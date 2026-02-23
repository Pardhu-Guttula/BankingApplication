# Epic Title: Persist Shopping Cart State in PostgreSQL

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.shopping_cart.repositories.cart_repository import CartRepository
from backend.shopping_cart.services.cart_service import CartService
from backend.product_catalog.repositories.product_repository import ProductRepository

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart/update', methods=['POST'])
def update_cart():
    db = next(get_db())
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    cart_repository = CartRepository(db)
    product_repository = ProductRepository(db)
    cart_service = CartService(cart_repository, product_repository)

    try:
        response = cart_service.update_product_quantity_in_cart(db, user_id, product_id, quantity)
        if isinstance(response, str):
            return jsonify({"error": response}), 404
        return jsonify([{
            "product_id": item.product_id,
            "quantity": item.quantity
        } for item in response])
    except SQLAlchemyError as se:
        return jsonify({"error": "Unable to process your request"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400

@cart_bp.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    db = next(get_db())
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')

    cart_repository = CartRepository(db)
    product_repository = ProductRepository(db)
    cart_service = CartService(cart_repository, product_repository)

    try:
        response = cart_service.remove_product_from_cart(db, user_id, product_id)
        if isinstance(response, str):
            return jsonify({"error": response}), 404
        return jsonify([{
            "product_id": item.product_id,
            "quantity": item.quantity
        } for item in response])
    except SQLAlchemyError as se:
        return jsonify({"error": "Unable to process your request"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400