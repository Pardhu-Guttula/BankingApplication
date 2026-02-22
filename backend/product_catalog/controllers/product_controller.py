# Epic Title: Filter Products by Category

from flask import Blueprint, jsonify, request
from backend.product_catalog.repositories.product_repository import ProductRepository

product_bp = Blueprint('product', __name__)
product_repository = ProductRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@product_bp.route('/products/category/<int:category_id>', methods=['GET'])
def get_products_by_category(category_id: int):
    try:
        products = product_repository.get_products_by_category(category_id)
        if products:
            return jsonify([product.__dict__ for product in products])
        else:
            return jsonify({'message': 'No products found in this category'}), 404
    except Exception as e:
        return jsonify({'error': 'Unable to retrieve products'}), 500