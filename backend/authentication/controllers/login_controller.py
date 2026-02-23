# Epic Title: Develop User Logout Capability

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.authentication.repositories.user_repository import UserRepository
from backend.authentication.repositories.session_repository import SessionRepository
from backend.authentication.services.login_service import LoginService

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login_user():
    db = next(get_db())
    user_repository = UserRepository(db)
    session_repository = SessionRepository(db)
    login_service = LoginService(user_repository, session_repository)

    try:
        data = request.get_json()

        email = data['email']
        password = data['password']

        token = login_service.authenticate_user(db, email, password)
        if token:
            return jsonify({"token": token}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except SQLAlchemyError as se:
        return jsonify({"error": "Database error occurred"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400