# Epic Title: Implement Multi-Factor Authentication (MFA)

import logging
from flask import Blueprint, request, jsonify
from backend.authentication.services.mfa_service import MFAService

# Controller for Multi-Factor Authentication (MFA)
mfa_controller = Blueprint('mfa_controller', __name__)
mfa_service = MFAService()

@mfa_controller.route('/request_otp', methods=['POST'])
def request_otp():
    try:
        data = request.json
        user_id = data.get('user_id')
        method = data.get('method')  # 'email', 'sms', or 'biometric'
        mfa_service.generate_otp(user_id, method)
        return jsonify({"message": "OTP sent successfully"}), 200
    except Exception as e:
        logging.error(f'Error in request_otp: {e}')
        return jsonify({"message": "OTP request failed"}), 500