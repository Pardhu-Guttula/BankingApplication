# Epic Title: Display Product Details

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.product_catalog.repositories.product_repository import ProductRepository
from backend.product_catalog.services.product_service import ProductService

product_bp = Blueprint('product', __name__)

@product_bp.route('/product/<int:product_id>', methods=['GET'])
def view_product_details(product_id: int):
    db = next(get_db())
    product_repository = ProductRepository(db)
    product_service = ProductService(product_repository)

    try:
        product_info = product_service.fetch_product_details(db, product_id)
        if isinstance(product_info, str):
            return jsonify({"error": product_info}), 404
        return jsonify({
            "name": product_info.name,
            "price": product_info.price,
            "description": product_info.description
        })
    except SQLAlchemyError as se:
        return jsonify({"error": "Unable to retrieve product details"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400