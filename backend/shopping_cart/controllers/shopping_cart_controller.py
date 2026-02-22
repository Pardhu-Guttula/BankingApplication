# Epic Title: Add products to the shopping cart

from flask import Blueprint, jsonify, request
from backend.shopping_cart.repositories.product_repository import ProductRepository
from backend.shopping_cart.repositories.shopping_cart_repository import ShoppingCartRepository

shopping_cart_bp = Blueprint('shopping_cart', __name__)
product_repository = ProductRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})
shopping_cart_repository = ShoppingCartRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@shopping_cart_bp.route('/cart/<int:user_id>/add', methods=['POST'])
def add_to_cart(user_id: int):
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)
    product = product_repository.get_product_by_id(product_id)
    
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    
    if not product.available:
        return jsonify({'error': 'Product is unavailable'}), 400
    
    success = shopping_cart_repository.add_item_to_cart(user_id, product, quantity)
    if not success:
        return jsonify({'error': 'Product is unavailable'}), 400
    
    cart = shopping_cart_repository.get_cart_by_user_id(user_id)
    return jsonify({
        'user_id': cart.user.id,
        'items': [{'product_id': item.product.id, 'name': item.product.name, 'price': item.product.price, 'description': item.product.description, 'quantity': item.quantity} for item in cart.items]
    })