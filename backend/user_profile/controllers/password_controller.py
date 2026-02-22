# Epic Title: Change Password

import logging
import bcrypt
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from backend.user_profile.repositories.user_repository import UserRepository

password_bp = Blueprint('password', __name__)
user_repository = UserRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@password_bp.route('/password/change', methods=['POST'])
@login_required
def change_password():
    data = request.get_json()
    
    if not data or not data.get('old_password') or not data.get('new_password'):
        return jsonify({'error': 'Invalid input'}), 400
    
    user_profile = user_repository.get_user_by_id(current_user.id)

    if not user_profile:
        return jsonify({'error': 'User not found'}), 404

    if not bcrypt.checkpw(data.get('old_password').encode('utf-8'), user_profile.hashed_password.encode('utf-8')):
        return jsonify({'error': 'Incorrect password'}), 400

    new_password = data.get('new_password')
    if not validate_password_complexity(new_password):
        return jsonify({'error': 'Password does not meet complexity requirements'}), 400

    new_hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    success = user_repository.update_password(current_user.id, new_hashed_password)
    
    if success:
        return jsonify({'message': 'Password changed successfully'}), 200
    else:
        return jsonify({'error': 'Failed to change password'}), 500

def validate_password_complexity(password: str) -> bool:
    # Placeholder function to check password complexity
    # Minimum length 8, at least one uppercase, one lowercase, one digit and one special character
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!@#$%^&*()-_=+[]{}|;:",.<>?/' for char in password):
        return False
    return True