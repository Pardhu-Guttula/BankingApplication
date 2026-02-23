# Epic Title: Implement Multi-Factor Authentication (MFA)

import logging
from flask import Blueprint, request, jsonify
from backend.user_authentication.services.mfa_service import MFAService

# Controller for Multi-Factor Authentication
mfa_controller = Blueprint('mfa_controller', __name__)
mfa_service = MFAService()

@mfa_controller.route('/mfa/send_otp', methods=['POST'])
def send_otp():
    try:
        data = request.json
        user_id = data.get("user_id")
        method = data.get("method")  # email, sms, or biometric
        otp_sent = mfa_service.send_otp(user_id, method)
        if otp_sent:
            return jsonify({"message": "OTP sent successfully"}), 200
        return jsonify({"message": "Failed to send OTP"}), 400
    except Exception as e:
        logging.error(f"Error in send_otp: {e}")
        return jsonify({"message": "Failed to send OTP"}), 500

@mfa_controller.route('/mfa/verify_otp', methods=['POST'])
def verify_otp():
    try:
        data = request.json
        user_id = data.get("user_id")
        otp = data.get("otp")
        is_valid = mfa_service.verify_otp(user_id, otp)
        if is_valid:
            return jsonify({"message": "OTP verified successfully"}), 200
        return jsonify({"message": "Invalid OTP"}), 400
    except Exception as e:
        logging.error(f"Error in verify_otp: {e}")
        return jsonify({"message": "Failed to verify OTP"}), 500

@mfa_controller.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if not name or not email or not password:
            return jsonify({'message': 'Name, email, and password are required.'}), 400
        registration_result = mfa_service.register_user(name, email, password)
        if registration_result['success']:
            return jsonify({'message': 'Registration successful. Please check your email to confirm your account.'}), 201
        else:
            return jsonify({'message': registration_result['message']}), 400
    except Exception as e:
        logging.error(f"Error in register: {e}")
        return jsonify({'message': 'Failed to register user.'}), 500

@mfa_controller.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')
        login_result = mfa_service.login_user(email, password)
        if login_result['success']:
            return jsonify({'message': 'Login successful', 'token': login_result['token']}), 200
        else:
            return jsonify({'message': login_result['message']}), 400
    except Exception as e:
        logging.error(f"Error in login: {e}")
        return jsonify({'message': 'Failed to log in user.'}), 500

@mfa_controller.route('/logout', methods=['POST'])
def logout():
    try:
        data = request.json
        token = data.get('token')
        logout_result = mfa_service.logout_user(token)
        if logout_result['success']:
            return jsonify({'message': 'Logout successful'}), 200
        else:
            return jsonify({'message': logout_result['message']}), 400
    except Exception as e:
        logging.error(f"Error in logout: {e}")
        return jsonify({'message': 'Failed to log out user.'}), 500

@mfa_controller.route('/change_role', methods=['POST'])
def change_user_role():
    try:
        data = request.json
        admin_token = data.get('admin_token')
        user_id = data.get('user_id')
        new_role = data.get('new_role')
        change_role_result = mfa_service.change_user_role(admin_token, user_id, new_role)
        if change_role_result['success']:
            return jsonify({'message': 'User role updated successfully.'}), 200
        else:
            return jsonify({'message': change_role_result['message']}), 400
    except Exception as e:
        logging.error(f"Error in change_user_role: {e}")
        return jsonify({'message': 'Failed to change user role.'}), 500
