# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.auth.session_service.py import SessionService

session_bp = Blueprint('session_bp', __name__)

@session_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user_id = data['user_id']
    service = SessionService()
    session_id = service.create_session(user_id)
    auth_token = service.create_auth_token(user_id)
    return jsonify({"session_id": session_id, "auth_token": auth_token}), 200

@session_bp.route('/validate', methods=['POST'])
def validate_token():
    data = request.json
    token = data['auth_token']
    service = SessionService()
    is_valid = service.validate_auth_token(token)
    if is_valid:
        return jsonify({"message": "Token is valid"}), 200
    return jsonify({"message": "Token is invalid or expired"}), 401

@session_bp.route('/logout', methods=['POST'])
def logout():
    data = request.json
    token = data['auth_token']
    service = SessionService()
    service.invalidate_auth_token(token)
    return jsonify({"message": "Logged out successfully"}), 200