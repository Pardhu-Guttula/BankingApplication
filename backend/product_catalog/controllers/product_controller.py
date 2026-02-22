# Epic Title: Display Product Details

from flask import Blueprint, jsonify, request
from backend.product_catalog.repositories.product_repository import ProductRepository

product_bp = Blueprint('product', __name__)
product_repository = ProductRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@product_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id: int):
    product = product_repository.get_product_by_id(product_id)
    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description
        })
    return jsonify({'error': 'Product details are not available'}), 404