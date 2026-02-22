# Epic Title: User Authentication and Authorization
import logging
from flask import Blueprint, request, jsonify
from backend.authentication.services.auth_service import AuthService

# Controller for Authentication
auth_controller = Blueprint('auth_controller', __name__)
auth_service = AuthService()

@auth_controller.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        if auth_service.authenticate(username, password):
            return jsonify({"message": "Login successful"}), 200
        return jsonify({"message": "Invalid credentials"}), 401
    except Exception as e:
        logging.error(f'Error in login: {e}')
        return jsonify({"message": "Login failed"}), 500
