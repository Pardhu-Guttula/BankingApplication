# Epic Title: Sort Products by Price

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.product_catalog.repositories.product_repository import ProductRepository
from backend.product_catalog.services.product_service import ProductService

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def list_products():
    db = next(get_db())
    product_repository = ProductRepository(db)
    product_service = ProductService(product_repository)
    sort_order = request.args.get('sort_order', default='', type=str)

    try:
        products = product_service.fetch_sorted_products(db, sort_order)
        if products:
            return jsonify([{
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description
            } for product in products])
        return jsonify({"message": "No products found"}), 404
    except SQLAlchemyError as se:
        return jsonify({"error": "Unable to retrieve sorting options"}), 500