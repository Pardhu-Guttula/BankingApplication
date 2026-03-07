# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.interaction_history.interaction_service import InteractionService
from backend.services.notifications.notification_service import NotificationService

interaction_bp = Blueprint('interaction_bp', __name__)

@interaction_bp.route('/interactions', methods=['GET'])
def get_interactions():
    user_id = request.args.get('user_id')
    service = InteractionService()
    interactions = service.get_interactions(user_id)
    return jsonify([interaction.__dict__ for interaction in interactions]), 200

@interaction_bp.route('/track_login', methods=['POST'])
def track_login():
    user_id = request.json['user_id']
    service = InteractionService()
    interaction = service.track_login(user_id)
    notification_service = NotificationService()
    notification_service.send_notification(user_id, "login", f"User {user_id} logged in successfully.")
    return jsonify({"message": "Login tracked successfully", "interaction_id": interaction.interaction_id}), 201

@interaction_bp.route('/track_data_export', methods=['POST'])
def track_data_export():
    user_id = request.json['user_id']
    service = InteractionService()
    interaction = service.track_data_export(user_id)
    notification_service = NotificationService()
    notification_service.send_notification(user_id, "data_export", f"User {user_id} exported their interaction history successfully.")
    return jsonify({"message": "Data export tracked successfully", "interaction_id": interaction.interaction_id}), 201

@interaction_bp.route('/track_anomaly_detection', methods=['POST'])
def track_anomaly_detection():
    user_id = request.json['user_id']
    message = request.json['message']
    service = InteractionService()
    interaction = service.track_anomaly_detection(user_id, message)
    notification_service = NotificationService()
    notification_service.send_notification(user_id, "anomaly_detection", f"Anomaly detected for user {user_id}: {message}")
    return jsonify({"message": "Anomaly detection tracked successfully", "interaction_id": interaction.interaction_id}), 201