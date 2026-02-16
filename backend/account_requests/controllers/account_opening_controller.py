# Epic Title: Simplify Account Opening Workflow

from flask import Blueprint, request, jsonify
from backend.account_requests.services.account_opening_service import AccountOpeningService

account_opening_controller = Blueprint('account_opening_controller', __name__)

@account_opening_controller.route('/account/open', methods=['POST'])
def open_account():
    data = request.get_json()
    user_id = data.get('user_id')
    
    if user_id is None:
        return jsonify({'error': 'User ID is required'}), 400

    success, message = AccountOpeningService.submit_account_opening_request(user_id)
    if success:
        return jsonify({'message': 'Account opening request submitted successfully'}), 200
    else:
        return jsonify({'error': message}), 400