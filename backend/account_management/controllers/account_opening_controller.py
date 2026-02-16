# Epic Title: Enable Account Opening Requests

import logging
from flask import Blueprint, request, jsonify
from backend.account_management.services.account_opening_service import AccountOpeningService

# Controller for Account Opening
account_opening_controller = Blueprint('account_opening_controller', __name__)
account_opening_service = AccountOpeningService()

@account_opening_controller.route('/account/open', methods=['POST'])
def open_account():
    try:
        data = request.json
        user_id = data.get("user_id")
        account_type = data.get("account_type")
        success = account_opening_service.submit_account_opening_request(user_id, account_type)
        if success:
            return jsonify({"message": "Account opening request submitted successfully"}), 200
        return jsonify({"message": "Failed to submit account opening request"}), 400
    except Exception as e:
        logging.error(f"Error in open_account: {e}")
        return jsonify({"message": "Failed to submit account opening request"}), 500