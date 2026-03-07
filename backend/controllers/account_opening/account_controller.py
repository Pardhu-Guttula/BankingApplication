# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.account_opening.account_service import AccountService

account_opening_bp = Blueprint('account_opening_bp', __name__)

@account_opening_bp.route('/open_account', methods=['POST'])
def open_account():
    data = request.json
    service = AccountService()
    account = service.create_account(
        user_id=data['user_id'],
        account_type=data['account_type'],
        initial_deposit=data['initial_deposit']
    )
    return jsonify({"message": "Account opened successfully", "account_id": account.account_id}), 201