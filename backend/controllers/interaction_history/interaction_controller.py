# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.interaction_history.interaction_service import InteractionService

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
    return jsonify({"message": "Login tracked successfully", "interaction_id": interaction.interaction_id}), 201

@interaction_bp.route('/track_page_visit', methods=['POST'])
def track_page_visit():
    user_id = request.json['user_id']
    location = request.json['location']
    service = InteractionService()
    interaction = service.track_page_visit(user_id, location)
    return jsonify({"message": "Page visit tracked successfully", "interaction_id": interaction.interaction_id}), 201

@interaction_bp.route('/track_form_submission', methods=['POST'])
def track_form_submission():
    user_id = request.json['user_id']
    location = request.json['location']
    service = InteractionService()
    interaction = service.track_form_submission(user_id, location)
    return jsonify({"message": "Form submission tracked successfully", "interaction_id": interaction.interaction_id}), 201