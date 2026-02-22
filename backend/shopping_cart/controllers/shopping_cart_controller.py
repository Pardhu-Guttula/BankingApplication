# Epic Title: Persist shopping cart state in PostgreSQL

from flask import Blueprint, jsonify, request
from backend.shopping_cart.repositories.shopping_cart_repository import ShoppingCartRepository
from backend.shopping_cart.repositories.product_repository import ProductRepository

shopping_cart_bp = Blueprint('shopping_cart', __name__)
product_repository = ProductRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'dbname': 'ecommerce'})
shopping_cart_repository = ShoppingCartRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'dbname': 'ecommerce'})

@shopping_cart_bp.route('/cart/<int:user_id>/add_or_update', methods=['POST'])
def add_or_update_cart(user_id: int):
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)
    
    if not isinstance(quantity, int) or quantity < 0:
        return jsonify({'error': 'Invalid quantity'}), 400

    product = product_repository.get_product_by_id(product_id)
    
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    
    success = shopping_cart_repository.add_or_update_item_in_cart(user_id, product_id, quantity)
    if not success and quantity > 0:
        return jsonify({'error': 'Requested quantity is not available'}), 400

    cart = shopping_cart_repository.get_cart_by_user_id(user_id)
    return jsonify({
        'user_id': cart.user.id,
        'items': [{'product_id': item.product.id, 'name': item.product.name, 'price': item.product.price, 'description': item.product.description, 'quantity': item.quantity} for item in cart.items]
    })

@shopping_cart_bp.route('/cart/<int:user_id>/remove', methods=['POST'])
def remove_from_cart(user_id: int):
    product_id = request.json.get('product_id')
    product = product_repository.get_product_by_id(product_id)
    
    if product is None:
        return jsonify({'error': 'Product not found'}), 404

    success = shopping_cart_repository.remove_item_from_cart(user_id, product_id)
    if not success:
        return jsonify({'error': 'Product not in cart'}), 400

    cart = shopping_cart_repository.get_cart_by_user_id(user_id)
    return jsonify({
        'user_id': cart.user.id,
        'items': [{'product_id': item.product.id, 'name': item.product.name, 'price': item.product.price, 'description': item.product.description, 'quantity': item.quantity} for item in cart.items]
    })