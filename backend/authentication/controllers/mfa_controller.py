# Epic Title: Implement Multi-Factor Authentication

from flask import Blueprint, request, jsonify
from backend.authentication.services.mfa_service import MFAService

mfa_controller = Blueprint('mfa_controller', __name__)

@mfa_controller.route('/mfa/send_code', methods=['POST'])
def send_code():
    data = request.get_json()
    user_id = data.get('user_id')
    method = data.get('method')
    
    if user_id is None or method is None:
        return jsonify({'error': 'Invalid data'}), 400

    success, error = MFAService.send_code(user_id, method)
    if success:
        return jsonify({'message': 'MFA code sent successfully'}), 200
    else:
        return jsonify({'error': error}), 400

@mfa_controller.route('/mfa/verify_code', methods=['POST'])
def verify_code():
    data = request.get_json()
    user_id = data.get('user_id')
    code = data.get('code')
    
    if user_id is None or code is None:
        return jsonify({'error': 'Invalid data'}), 400

    success, error = MFAService.verify_code(user_id, code)
    if success:
        return jsonify({'message': 'MFA verified successfully'}), 200
    else:
        return jsonify({'error': error}), 400