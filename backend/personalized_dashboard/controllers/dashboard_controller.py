# Epic Title: Display Personalized Banking Products

import logging
from flask import Blueprint, request, jsonify
from backend.personalized_dashboard.services.dashboard_service import DashboardService

# Controller for Personalized Dashboard
dashboard_controller = Blueprint('dashboard_controller', __name__)
dashboard_service = DashboardService()

@dashboard_controller.route('/dashboard', methods=['GET'])
def get_personalized_dashboard():
    try:
        user_id = request.args.get("user_id")
        personalized_data = dashboard_service.get_personalized_dashboard(user_id)
        return jsonify(personalized_data), 200
    except Exception as e:
        logging.error(f"Error in get_personalized_dashboard: {e}")
        return jsonify({"message": "Failed to retrieve dashboard"}), 500