# Epic Title: Implement Account Lockout Mechanism

from flask import Blueprint, request, jsonify
from backend.authentication.services.account_lock_service import AccountLockService

account_lock_controller = Blueprint('account_lock_controller', __name__)

@account_lock_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_id = data.get('user_id')
    password = data.get('password')

    if user_id is None or password is None:
        return jsonify({'error': 'Invalid data'}), 400

    success, message = AccountLockService.process_login(user_id, password)
    if success:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': message}), 400