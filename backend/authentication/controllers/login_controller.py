# Epic Title: Implement Account Lockout Mechanism

from flask import Blueprint, request, jsonify
from backend.authentication.services.login_service import LoginService

login_controller = Blueprint('login_controller', __name__)

@login_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    authenticated = LoginService.authenticate_user(username, password)
    if authenticated:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials or account locked'}), 401