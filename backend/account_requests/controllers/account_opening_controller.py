# Epic Title: Simplify Account Opening Workflow

from flask import Blueprint, request, jsonify
from backend.account_requests.services.account_opening_service import AccountOpeningService

account_opening_controller = Blueprint('account_opening_controller', __name__)

@account_opening_controller.route('/account/open', methods=['POST'])
def open_account():
    data = request.get_json()
    user_id = data.get('user_id')
    account_type = data.get('account_type')

    if not user_id or not account_type:
        return jsonify({'error': 'User ID and account type are required'}), 400

    response = AccountOpeningService.submit_account_opening_request(user_id, account_type)
    return jsonify(response), 200