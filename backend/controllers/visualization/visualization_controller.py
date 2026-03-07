# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.interaction_history.interaction_service import InteractionService
from backend.services.visualization.visualization_service import VisualizationService

visualization_bp = Blueprint('visualization_bp', __name__)

@visualization_bp.route('/visualize_interaction_history', methods=['GET'])
def visualize_interaction_history():
    user_id = request.args.get('user_id')
    interaction_type = request.args.get('interaction_type')
    
    service = InteractionService()
    interactions = service.get_interactions(user_id, interaction_type)
    
    filename = VisualizationService.visualize_interaction_history(interactions, interaction_type)
    
    return jsonify({"message": f"{interaction_type.capitalize()} history visualized successfully", "filename": filename}), 200