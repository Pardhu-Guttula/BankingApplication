# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.interaction_history.interaction_service import InteractionService

interaction_bp = Blueprint('interaction_bp', __name__)

@interaction_bp.route('/interactions', methods=['GET'])
def get_interactions():
    user_id = request.args.get('user_id')
    requested_user_id = request.args.get('requested_user_id')
    service = InteractionService()
    if not service.verify_access_control(user_id, requested_user_id):
        return jsonify({"error": "Access denied"}), 403
    interactions = service.get_interactions(user_id)
    return jsonify([interaction.__dict__ for interaction in interactions]), 200

@interaction_bp.route('/add_interaction', methods=['POST'])
def add_interaction():
    data = request.json
    service = InteractionService()
    interaction = service.add_interaction(
        interaction_id=data['interaction_id'],
        user_id=data['user_id'],
        interaction_type=data['interaction_type'],
        timestamp=data['timestamp'],
        location=data['location']
    )
    return jsonify({"message": "Interaction added successfully", "interaction_id": interaction.interaction_id}), 201

@interaction_bp.route('/anonymized_interactions', methods=['GET'])
def get_anonymized_interactions():
    service = InteractionService()
    interactions = service.get_anonymized_interactions()
    return jsonify([interaction.__dict__ for interaction in interactions]), 200