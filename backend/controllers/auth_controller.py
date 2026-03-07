# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.auth.authentication_service import AuthenticationService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    service = AuthenticationService()
    token = service.login(username, password)
    if token:
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    data = request.json
    token = data['token']
    service = AuthenticationService()
    service.logout(token)
    return jsonify({"message": "Logged out successfully"}), 200

@auth_bp.route('/validate', methods=['POST'])
def validate_token():
    data = request.json
    token = data['token']
    service = AuthenticationService()
    is_valid = service.validate_token(token)
    if is_valid:
        return jsonify({"message": "Token is valid"}), 200
    return jsonify({"message": "Token is invalid or expired"}), 401