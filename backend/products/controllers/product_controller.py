# Epic Title: Create Products Table in PostgreSQL

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.products.repositories.product_repository import ProductRepository
from backend.products.services.product_service import ProductService

product_bp = Blueprint('product', __name__)

@product_bp.route('/add', methods=['POST'])
def add_product():
    db = next(get_db())
    product_repository = ProductRepository(db)
    product_service = ProductService(product_repository)

    try:
        data = request.get_json()

        name = data['name']
        price = data['price']

        new_product = product_service.add_product(db, name, price)
        return jsonify({"message": "Product added successfully"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except SQLAlchemyError as se:
        return jsonify({"error": "Database error occurred"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400