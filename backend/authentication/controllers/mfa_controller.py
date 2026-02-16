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

@mfa_controller.route('/mfa/encrypt_data', methods=['POST'])
def encrypt_data():
    data = request.get_json()
    financial_data = data.get('financial_data')

    if not financial_data:
        return jsonify({'error': 'Financial data is missing'}), 400

    encrypted_data = MFAService.encrypt_financial_data(financial_data)
    return jsonify({'encrypted_data': encrypted_data}), 200

@mfa_controller.route('/mfa/recover_password', methods=['POST'])
def recover_password():
    data = request.get_json()
    username = data.get('username')

    user = MFARepository.get_user_by_username(username)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    MFAService.send_password_recovery_email(user)
    return jsonify({'message': 'Password recovery email sent'}), 200

@mfa_controller.route('/mfa/account_lockout', methods=['POST'])
def account_lockout():
    data = request.get_json()
    username = data.get('username')
    attempts = data.get('attempts')

    if attempts >= 5:
        user = MFARepository.get_user_by_username(username)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        MFAService.lock_user_account(user)
        return jsonify({'message': 'User account locked'}), 200
    else:
        return jsonify({'message': 'Attempts below threshold, account not locked'}), 200