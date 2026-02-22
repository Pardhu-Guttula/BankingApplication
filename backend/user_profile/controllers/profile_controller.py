# Epic Title: Update Personal Information

import logging
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.user_profile.models.user_profile import UserProfile
from backend.user_profile.repositories.user_repository import UserRepository
import datetime

profile_bp = Blueprint('profile', __name__)
user_repository = UserRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@profile_bp.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Invalid input'}), 400
    
    try:
        user_profile = UserProfile(
            user_id=current_user.id,
            name=data.get('name'),
            email=data.get('email'),
            address=data.get('address'),
            updated_at=datetime.datetime.now()
        )
        success = user_repository.update_user_profile(user_profile)
        
        if success:
            return jsonify({'message': 'Profile updated successfully'}), 200
        else:
            return jsonify({'error': 'Failed to update profile'}), 500
    except Exception as e:
        logging.error(f'Error updating profile: {e}')
        return jsonify({'error': 'Invalid input'}), 400