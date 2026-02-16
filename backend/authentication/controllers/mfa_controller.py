# Epic Title: Implement Multi-Factor Authentication (MFA)

import logging
from flask import Blueprint, request, jsonify
from backend.authentication.services.mfa_service import MFAService

# Controller for Multi-Factor Authentication
mfa_controller = Blueprint('mfa_controller', __name__)
mfa_service = MFAService()

@mfa_controller.route('/mfa/request_otp', methods=['POST'])
def request_otp():
    try:
        data = request.json
        user_id = data.get("user_id")
        otp_method = data.get("otp_method")  # 'email' or 'sms'
        if mfa_service.send_otp(user_id, otp_method):
            return jsonify({"message": "OTP sent successfully"}), 200
        return jsonify({"message": "Failed to send OTP"}), 400
    except Exception as e:
        logging.error(f"Error in request_otp: {e}")
        return jsonify({"message": "Failed to request OTP"}), 500

@mfa_controller.route('/mfa/verify_otp', methods=['POST'])
def verify_otp():
    try:
        data = request.json
        user_id = data.get("user_id")
        otp = data.get("otp")
        if mfa_service.verify_otp(user_id, otp):
            return jsonify({"message": "OTP verified successfully"}), 200
        return jsonify({"message": "Failed to verify OTP"}), 400
    except Exception as e:
        logging.error(f"Error in verify_otp: {e}")
        return jsonify({"message": "Failed to verify OTP"}), 500