# Epic Title: Display Banking Products Dynamically

from flask import Blueprint, jsonify, request
from backend.dashboard.services.product_service import ProductService

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/dashboard/products', methods=['GET'])
def get_products():
    user_id = request.args.get('user_id')
    
    if user_id is None:
        return jsonify({'error': 'User ID is required'}), 400

    products = ProductService.get_products_for_user(user_id)
    return jsonify(products), 200