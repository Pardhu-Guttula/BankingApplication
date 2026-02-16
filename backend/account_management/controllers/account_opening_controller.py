# Epic Title: Enable Account Opening Requests

import logging
from flask import Blueprint, request, jsonify
from backend.account_management.services.account_opening_service import AccountOpeningService

# Controller for Account Opening Requests
account_opening_controller = Blueprint('account_opening_controller', __name__)
account_opening_service = AccountOpeningService()

@account_opening_controller.route('/account/open', methods=['POST'])
def open_account():
    try:
        data = request.json
        user_id = data.get("user_id")
        account_type = data.get("account_type")
        initial_deposit = data.get("initial_deposit")
        if account_opening_service.submit_account_request(user_id, account_type, initial_deposit):
            return jsonify({"message": "Account opening request submitted successfully"}), 201
        return jsonify({"message": "Failed to submit account opening request"}), 400
    except Exception as e:
        logging.error(f"Error in open_account: {e}")
        return jsonify({"message": "Account opening request failed"}), 500