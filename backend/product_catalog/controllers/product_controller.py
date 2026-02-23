# Epic Title: Filter Products by Category

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
    category_id = request.args.get('category_id', type=int)

    try:
        if category_id:
            products = db.query(Product).filter(Product.category_id == category_id).all()
        else:
            products = db.query(Product).all()
        if products:
            return jsonify([{
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description
            } for product in products])
        return jsonify({"message": "No products found in this category"}), 404
    except SQLAlchemyError as se:
        return jsonify({"error": "Unable to retrieve products"}), 500