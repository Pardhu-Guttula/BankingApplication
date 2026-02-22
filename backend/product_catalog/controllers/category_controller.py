# Epic Title: Filter Products by Category

from flask import Blueprint, jsonify
from backend.product_catalog.repositories.category_repository import CategoryRepository

category_bp = Blueprint('category', __name__)
category_repository = CategoryRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    try:
        categories = category_repository.get_all_categories()
        return jsonify([category.__dict__ for category in categories])
    except Exception as e:
        return jsonify({'error': 'Unable to retrieve filter options'}), 500