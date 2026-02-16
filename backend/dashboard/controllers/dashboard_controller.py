# Epic Title: Design User Profile-Based Dashboard

from flask import Blueprint, jsonify, request
from backend.dashboard.services.dashboard_service import DashboardService

dashboard_controller = Blueprint('dashboard_controller', __name__)

@dashboard_controller.route('/dashboard/personalized', methods=['GET'])
def personalized_dashboard():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    dashboard_data = DashboardService.get_personalized_dashboard(int(user_id))
    if not dashboard_data:
        return jsonify({'error': 'User profile not found'}), 404

    return jsonify(dashboard_data), 200