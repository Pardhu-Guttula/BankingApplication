# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.interaction_history.interaction_service import InteractionService

interaction_bp = Blueprint('interaction_bp', __name__)

@interaction_bp.route('/search_interactions', methods=['GET'])
def search_interactions():
    event_type = request.args.get('event_type')
    service = InteractionService()
    interactions = service.search_interactions(event_type)
    return jsonify([interaction.__dict__ for interaction in interactions]), 200