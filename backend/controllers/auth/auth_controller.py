# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.auth.auth_service import AuthService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    service = AuthService()
    user = service.get_user(user_id)
    return jsonify(user.__dict__), 200

@auth_bp.route('/authorized_action', methods=['POST'])
def perform_authorized_action():
    data = request.json
    user_id = data['user_id']
    required_permission = data['required_permission']
    service = AuthService()
    authorized = service.perform_authorized_action(user_id, required_permission)
    if authorized:
        return jsonify({"message": "Action authorized"}), 200
    else:
        return jsonify({"message": "Action not authorized"}), 403