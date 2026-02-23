# Epic Title: Filter Products by Category

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.product_catalog.repositories.category_repository import CategoryRepository
from backend.product_catalog.services.category_service import CategoryService

category_bp = Blueprint('category', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    db = next(get_db())
    category_repository = CategoryRepository(db)
    category_service = CategoryService(category_repository)

    try:
        categories = category_service.fetch_all_categories(db)
        return jsonify([{"id": category.id, "name": category.name} for category in categories])
    except SQLAlchemyError as se:
        return jsonify({"error": "Unable to retrieve filter options"}), 500