# Epic Title: Manage Account

import logging
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
import datetime
from backend.account_management.models.account_settings import AccountSettings
from backend.account_management.repositories.account_repository import AccountRepository

account_bp = Blueprint('account', __name__)
account_repository = AccountRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@account_bp.route('/account/settings', methods=['POST'])
@login_required
def update_account_settings():
    data = request.get_json()
    
    if not data or not data.get('preferences') or not data.get('privacy_settings'):
        return jsonify({'error': 'Invalid input'}), 400
    
    account_settings = AccountSettings(
        user_id=current_user.id,
        preferences=data.get('preferences'),
        privacy_settings=data.get('privacy_settings'),
        updated_at=datetime.datetime.now()
    )
    
    success = account_repository.update_account_settings(account_settings)
    
    if success:
        return jsonify({'message': 'Account settings updated successfully'}), 200
    else:
        return jsonify({'error': 'Failed to update account settings'}), 500