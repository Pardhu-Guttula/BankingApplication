# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.auth.auth_service import AuthService

log_bp = Blueprint('log_bp', __name__)

@log_bp.route('/logs', methods=['GET'])
def get_logs():
    action = request.args.get('action')
    service = AuthService()
    logs = service.get_logs(action)
    return jsonify([log.__dict__ for log in logs]), 200