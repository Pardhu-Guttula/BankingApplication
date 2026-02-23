# Epic Title: Develop User Registration Capability

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.authentication.repositories.user_repository import UserRepository
from backend.authentication.services.registration_service import RegistrationService

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/register', methods=['POST'])
def register_user():
    db = next(get_db())
    user_repository = UserRepository(db)
    registration_service = RegistrationService(user_repository)

    try:
        data = request.get_json()

        name = data['name']
        email = data['email']
        password = data['password']

        new_user = registration_service.register_user(db, name, email, password)
        return jsonify({"message": "User registered successfully"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except SQLAlchemyError as se:
        return jsonify({"error": "Database error occurred"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400