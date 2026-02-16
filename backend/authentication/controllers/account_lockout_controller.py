# Epic Title: Implement Account Lockout Mechanism

from flask import Blueprint, request, jsonify
from backend.authentication.services.account_lockout_service import AccountLockoutService

account_lockout_controller = Blueprint('account_lockout_controller', __name__)

@account_lockout_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_id = data.get('user_id')
    password = data.get('password')

    if user_id is None or password is None:
        return jsonify({'error': 'Invalid data'}), 400

    # Placeholder for actual authentication logic
    success = True  # Replace with actual authentication check
    locked, message = AccountLockoutService.record_attempt_and_check_lockout(user_id, success)

    if locked:
        return jsonify({'error': message}), 423  # 423 Locked
    elif not success:
        return jsonify({'error': message}), 401  # 401 Unauthorized
    else:
        return jsonify({'message': message}), 200