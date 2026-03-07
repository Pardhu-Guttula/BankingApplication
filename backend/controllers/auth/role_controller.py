# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.auth.role_service import RoleService

role_bp = Blueprint('role_bp', __name__)

@role_bp.route('/roles', methods=['GET'])
def get_all_roles():
    service = RoleService()
    roles = service.get_all_roles()
    return jsonify([role.__dict__ for role in roles]), 200

@role_bp.route('/role/<role_id>', methods=['GET'])
def get_role(role_id):
    service = RoleService()
    role = service.get_role(role_id)
    return jsonify(role.__dict__), 200

@role_bp.route('/role', methods=['POST'])
def create_role():
    data = request.json
    role_id = data['role_id']
    role_name = data['role_name']
    service = RoleService()
    service.create_role(role_id, role_name)
    return jsonify({"message": "Role created successfully"}), 200

@role_bp.route('/role/<role_id>', methods=['PUT'])
def update_role(role_id):
    data = request.json
    role_name = data['role_name']
    service = RoleService()
    service.update_role(role_id, role_name)
    return jsonify({"message": "Role updated successfully"}), 200