# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.auth.user_service import UserService

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    service = UserService()
    user = service.get_user(user_id)
    return jsonify(user.__dict__), 200

@user_bp.route('/assign_role', methods=['POST'])
def assign_role():
    data = request.json
    user_id = data['user_id']
    role_name = data['role_name']
    service = UserService()
    service.assign_role(user_id, role_name)
    return jsonify({"message": "Role assigned successfully"}), 200

@user_bp.route('/revoke_role', methods=['POST'])
def revoke_role():
    data = request.json
    user_id = data['user_id']
    role_name = data['role_name']
    service = UserService()
    service.revoke_role(user_id, role_name)
    return jsonify({"message": "Role revoked successfully"}), 200