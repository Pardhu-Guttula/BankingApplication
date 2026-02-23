# Epic Title: Update Personal Information

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.user_profile.repositories.user_profile_repository import UserProfileRepository
from backend.user_profile.services.user_profile_service import UserProfileService

user_profile_bp = Blueprint('user_profile', __name__)

@user_profile_bp.route('/profile/update', methods=['POST'])
def update_user_profile():
    db = next(get_db())
    data = request.get_json()

    user_id = data.get('user_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    address = data.get('address')

    user_profile_repository = UserProfileRepository(db)
    user_profile_service = UserProfileService(user_profile_repository)

    try:
        user_profile = user_profile_service.update_user_profile(db, user_id, first_name, last_name, email, phone_number, address)
        if user_profile:
            return jsonify({
                "user_id": user_profile.user_id,
                "first_name": user_profile.first_name,
                "last_name": user_profile.last_name,
                "email": user_profile.email,
                "phone_number": user_profile.phone_number,
                "address": user_profile.address,
                "updated_at": user_profile.updated_at
            }), 200
        return jsonify({"error": "User profile not found"}), 404
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400