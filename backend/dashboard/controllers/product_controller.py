# Epic Title: Display Banking Products Dynamically

from flask import Blueprint, jsonify, request
from backend.dashboard.services.product_service import ProductService

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/dashboard/products', methods=['GET'])
def get_user_products():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    product_data = ProductService.get_dynamic_products(int(user_id))
    if not product_data:
        return jsonify({'error': 'User profile not found'}), 404

    return jsonify(product_data), 200