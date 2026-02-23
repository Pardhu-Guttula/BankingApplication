# Epic Title: Ensure Secure Storage and Retrieval

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.user_profile.repositories.user_repository import UserRepository
from backend.user_profile.services.user_service import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/users/change_password', methods=['POST'])
def change_password():
    db = next(get_db())
    data = request.get_json()

    user_id = data.get('user_id')
    old_password = data.get('old_password')
    new_password = data.get('new_password')

    user_repository = UserRepository(db)
    user_service = UserService(user_repository)

    try:
        result = user_service.change_password(db, user_id, old_password, new_password)
        if result['success']:
            return jsonify({"message": "Password changed successfully"}), 200
        return jsonify({"error": result.get("error")}), 400
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500