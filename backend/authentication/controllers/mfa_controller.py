# Epic Title: Implement Multi-Factor Authentication

from flask import Blueprint, request, jsonify
from backend.authentication.services.mfa_service import MFAService
from backend.authentication.repositories.mfa_repository import MFARepository

mfa_controller = Blueprint('mfa_controller', __name__)

@mfa_controller.route('/mfa/send_token', methods=['POST'])
def send_mfa_token():
    data = request.get_json()
    username = data.get('username')
    token_type = data.get('token_type')

    user = MFARepository.get_user_by_username(username)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    token = MFAService.send_mfa_token(user, token_type)
    return jsonify({'message': 'MFA token sent'}), 200

@mfa_controller.route('/mfa/verify_token', methods=['POST'])
def verify_mfa_token():
    data = request.get_json()
    username = data.get('username')
    token = data.get('token')
    token_type = data.get('token_type')

    user = MFARepository.get_user_by_username(username)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    is_valid = MFAService.verify_mfa_token(user, token, token_type)
    if is_valid:
        return jsonify({'message': 'MFA token verified'}), 200
    else:
        return jsonify({'error': 'Invalid or expired MFA token'}), 400