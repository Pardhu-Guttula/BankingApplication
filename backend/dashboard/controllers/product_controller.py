# Epic Title: Display Banking Products Dynamically

from flask import Blueprint, request, jsonify
from backend.dashboard.services.product_service import ProductService

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/products', methods=['GET'])
def fetch_products():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    product_data = ProductService.fetch_dynamic_products(int(user_id))
    return jsonify(product_data), 200