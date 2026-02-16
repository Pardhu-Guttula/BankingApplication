# Epic Title: Design User Profile-Based Dashboard

from flask import Blueprint, request, jsonify
from backend.dashboard.services.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard', methods=['GET'])
def get_dashboard():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    dashboard_content = DashboardService.get_personalized_dashboard(int(user_id))
    return jsonify(dashboard_content), 200