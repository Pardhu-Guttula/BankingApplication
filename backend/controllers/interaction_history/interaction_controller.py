# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.interaction_history.interaction_service import InteractionService

interaction_bp = Blueprint('interaction_bp', __name__)

@interaction_bp.route('/interactions', methods=['GET'])
def get_interactions():
    user_id = request.args.get('user_id')
    interaction_type = request.args.get('interaction_type')
    service = InteractionService()
    interactions = service.get_interactions(user_id, interaction_type)
    return jsonify([interaction.__dict__ for interaction in interactions]), 200