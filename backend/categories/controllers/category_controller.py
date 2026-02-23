# Epic Title: Create Categories Table in PostgreSQL

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.categories.repositories.category_repository import CategoryRepository
from backend.categories.services.category_service import CategoryService

category_bp = Blueprint('category', __name__)

@category_bp.route('/add', methods=['POST'])
def add_category():
    db = next(get_db())
    category_repository = CategoryRepository(db)
    category_service = CategoryService(category_repository)

    try:
        data = request.get_json()

        name = data['name']
        parent_category_id = data.get('parent_category_id')

        new_category = category_service.add_category(db, name, parent_category_id)
        return jsonify({"message": "Category added successfully"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except SQLAlchemyError as se:
        return jsonify({"error": "Database error occurred"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400