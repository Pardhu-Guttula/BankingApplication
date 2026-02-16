# Epic Title: Implement Multi-Factor Authentication

from flask import Blueprint, request, jsonify
from backend.authentication.services.mfa_service import MFAService

mfa_controller = Blueprint('mfa_controller', __name__)

@mfa_controller.route('/mfa/setup', methods=['POST'])
def setup_mfa():
    data = request.get_json()
    user_id = data.get('user_id')
    mfa_type = data.get('mfa_type')

    if not user_id or not mfa_type:
        return jsonify({'error': 'User ID and MFA type are required'}), 400

    mfa_details = MFAService.setup_mfa(user_id, mfa_type)
    return jsonify(mfa_details), 201

@mfa_controller.route('/mfa/verify', methods=['POST'])
def verify_mfa():
    data = request.get_json()
    user_id = data.get('user_id')
    mfa_code = data.get('mfa_code')

    if not user_id or not mfa_code:
        return jsonify({'error': 'User ID and MFA code are required'}), 400

    is_verified = MFAService.verify_mfa(user_id, mfa_code)
    if is_verified:
        return jsonify({'message': 'MFA verification successful'}), 200
    else:
        return jsonify({'error': 'MFA verification failed'}), 400