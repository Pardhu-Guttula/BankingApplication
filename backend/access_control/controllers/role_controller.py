# Epic Title: Implement user authentication and authorization features

from flask import Flask, request, jsonify
from backend.access_control.services.role_service import RoleService
from backend.access_control.repositories.role_repository import RoleRepository
from backend.access_control.repositories.user_repository import UserRepository

app = Flask(__name__)
role_repository = RoleRepository()
user_repository = UserRepository()
role_service = RoleService(role_repository, user_repository)

@app.route('/assign-role', methods=['POST'])
def assign_role():
    data = request.json
    user_email = data.get("email")
    role_name = data.get("role")
    if role_service.assign_role(user_email, role_name):
        return jsonify({"message": "Role assigned successfully"}), 200
    return jsonify({"error": "Failed to assign role"}), 400

@app.route('/permissions', methods=['GET'])
def get_permissions():
    email = request.args.get("email")
    permissions = role_service.get_permissions(email)
    return jsonify({"permissions": permissions}), 200