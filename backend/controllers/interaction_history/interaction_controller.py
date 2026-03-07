# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.interaction_history.interaction_service import InteractionService

interaction_bp = Blueprint('interaction_bp', __name__)

@interaction_bp.route('/interactions', methods=['GET'])
def get_interactions():
    user_id = request.args.get('user_id')
    date_start = request.args.get('date_start')
    date_end = request.args.get('date_end')
    interaction_type = request.args.get('interaction_type')
    search_query = request.args.get('search_query')
    service = InteractionService()
    interactions = service.get_interactions(user_id, date_start, date_end, interaction_type, search_query)
    return jsonify([interaction.__dict__ for interaction in interactions]), 200