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