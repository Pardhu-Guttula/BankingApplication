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

@auth_controller.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if auth_service.register(name, email, password):
            return jsonify({"message": "Registration successful. Please check your email for confirmation."}), 201
        return jsonify({"message": "Registration failed, email may already be in use."}), 400
    except Exception as e:
        logging.error(f'Error in registration: {e}')
        return jsonify({"message": "Registration failed"}), 500

@auth_controller.route('/logout', methods=['POST'])
def logout():
    try:
        auth_service.logout()
        return jsonify({"message": "Logout successful"}), 200
    except Exception as e:
        logging.error(f'Error in logout: {e}')
        return jsonify({"message": "Logout failed"}), 500