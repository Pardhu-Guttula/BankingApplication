# Epic Title: Simplify Account Opening Workflow

from flask import Blueprint, request, jsonify
from backend.account_requests.services.account_request_service import AccountRequestService

account_request_controller = Blueprint('account_request_controller', __name__)

@account_request_controller.route('/account_requests', methods=['POST'])
def submit_account_request():
    data = request.get_json()
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    account_request = AccountRequestService.submit_account_request(user_id)
    return jsonify({
        'message': 'Account request submitted successfully',
        'request_id': account_request.id
    }), 201