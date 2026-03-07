# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request, send_file
from backend.services.interaction_history.interaction_service import InteractionService

interaction_bp = Blueprint('interaction_bp', __name__)

@interaction_bp.route('/interactions', methods=['GET'])
def get_interactions():
    user_id = request.args.get('user_id')
    date_start = request.args.get('date_start')
    date_end = request.args.get('date_end')
    service = InteractionService()
    interactions = service.get_interactions(user_id, date_start, date_end)
    return jsonify([interaction.__dict__ for interaction in interactions]), 200

@interaction_bp.route('/export_interactions_csv', methods=['GET'])
def export_interactions_csv():
    user_id = request.args.get('user_id')
    date_start = request.args.get('date_start')
    date_end = request.args.get('date_end')
    service = InteractionService()
    file_path = service.export_interactions_csv(user_id, date_start, date_end)
    return send_file(file_path, as_attachment=True)

@interaction_bp.route('/export_interactions_pdf', methods=['GET'])
def export_interactions_pdf():
    user_id = request.args.get('user_id')
    date_start = request.args.get('date_start')
    date_end = request.args.get('date_end')
    service = InteractionService()
    file_path = service.export_interactions_pdf(user_id, date_start, date_end)
    return send_file(file_path, as_attachment=True)