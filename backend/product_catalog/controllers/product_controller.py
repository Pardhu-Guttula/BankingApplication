# Epic Title: Sort Products by Price

from flask import Blueprint, jsonify, request
from backend.product_catalog.repositories.product_repository import ProductRepository

product_bp = Blueprint('product', __name__)
product_repository = ProductRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@product_bp.route('/products/sort', methods=['GET'])
def get_products_sorted_by_price():
    order = request.args.get('order', 'ASC')
    if order not in ['ASC', 'DESC']:
        return jsonify({'error': 'Invalid sort option'}), 400

    try:
        products = product_repository.get_products_sorted_by_price(order)
        return jsonify([product.__dict__ for product in products])
    except Exception as e:
        return jsonify({'error': 'Unable to retrieve sorting options'}), 500