# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.dashboard.banking_product_service import BankingProductService

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    service = BankingProductService()
    product = service.add_banking_product(data['product_id'], data['name'], data['description'], data['eligibility_criteria'])
    return jsonify({"message": "Banking product added successfully"}), 201

@dashboard_bp.route('/products', methods=['GET'])
def get_all_products():
    service = BankingProductService()
    products = service.get_all_products()
    return jsonify([{
        "product_id": product.product_id,
        "name": product.name,
        "description": product.description,
        "eligibility_criteria": product.eligibility_criteria
    } for product in products])

@dashboard_bp.route('/eligible_products', methods=['GET'])
def get_eligible_products():
    eligibility_criteria = request.args.get('eligibility_criteria')
    service = BankingProductService()
    products = service.get_eligible_products(eligibility_criteria)
    return jsonify([{
        "product_id": product.product_id,
        "name": product.name,
        "description": product.description,
        "eligibility_criteria": product.eligibility_criteria
    } for product in products])

@dashboard_bp.route('/product_details/<product_id>', methods=['GET'])
def get_product_details(product_id):
    service = BankingProductService()
    product = service.get_product_details(product_id)
    if product:
        return jsonify({
            "product_id": product.product_id,
            "name": product.name,
            "description": product.description,
            "eligibility_criteria": product.eligibility_criteria
        })
    else:
        return jsonify({"message": "Product not found"}), 404