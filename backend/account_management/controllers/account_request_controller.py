# Epic Title: Enable Account Opening Requests

import logging
from flask import Blueprint, request, jsonify
from backend.account_management.services.account_request_service import AccountRequestService

# Controller for Account Opening Requests
account_request_controller = Blueprint('account_request_controller', __name__)
account_request_service = AccountRequestService()

@account_request_controller.route('/account/open', methods=['POST'])
def submit_account_request():
    try:
        data = request.json
        user_id = data.get('user_id')
        account_type = data.get('account_type')
        if account_request_service.submit_request(user_id, account_type):
            return jsonify({"message": "Account opening request submitted successfully"}), 201
        return jsonify({"message": "Failed to submit account opening request"}), 400
    except Exception as e:
        logging.error(f'Error in submit_account_request: {e}')
        return jsonify({"message": "Request submission failed"}), 500