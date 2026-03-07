# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.interaction_history.interaction_service import InteractionService

interaction_bp = Blueprint('interaction_bp', __name__)

@interaction_bp.route('/interactions', methods=['GET'])
def get_interactions():
    interaction_type = request.args.get('interaction_type')
    service = InteractionService()
    interactions = service.get_interactions(interaction_type)
    return jsonify([interaction.__dict__ for interaction in interactions]), 200

@interaction_bp.route('/add_interaction', methods=['POST'])
def add_interaction():
    data = request.json
    service = InteractionService()
    interaction = service.add_interaction(
        interaction_id=data['interaction_id'],
        user_id=data['user_id'],
        interaction_type=data['interaction_type'],
        timestamp=data['timestamp']
    )
    return jsonify({"message": "Interaction added successfully", "interaction_id": interaction.interaction_id}), 201