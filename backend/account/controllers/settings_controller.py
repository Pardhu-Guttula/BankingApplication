# Epic Title: Manage Account

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.account.repositories.account_settings_repository import AccountSettingsRepository
from backend.account.services.account_settings_service import AccountSettingsService

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/settings/update', methods=['POST'])
def update_account_settings():
    db = next(get_db())
    data = request.get_json()

    user_id = data.get('user_id')
    email_notifications = data.get('email_notifications')
    sms_notifications = data.get('sms_notifications')
    dark_mode = data.get('dark_mode')
    privacy_settings = data.get('privacy_settings')

    settings_repository = AccountSettingsRepository(db)
    settings_service = AccountSettingsService(settings_repository)

    try:
        settings = settings_service.update_account_settings(db, user_id, email_notifications, sms_notifications, dark_mode, privacy_settings)
        if settings:
            return jsonify({
                "user_id": settings.user_id,
                "email_notifications": settings.email_notifications,
                "sms_notifications": settings.sms_notifications,
                "dark_mode": settings.dark_mode,
                "privacy_settings": settings.privacy_settings,
                "updated_at": settings.updated_at
            }), 200
        return jsonify({"error": "Account settings not found"}), 404
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400