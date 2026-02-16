# Epic Title: Intuitive Dashboard Interface

import logging
from flask import Blueprint, render_template
from backend.personalized_dashboard.services.dashboard_service import DashboardService

# Controller for Personalized Dashboard UI
dashboard_ui_controller = Blueprint('dashboard_ui_controller', __name__)
dashboard_service = DashboardService()

@dashboard_ui_controller.route('/dashboard/<int:user_id>', methods=['GET'])
def show_dashboard(user_id: int):
    try:
        personalized_data = dashboard_service.get_personalized_data(user_id)
        return render_template('dashboard.html', data=personalized_data)
    except Exception as e:
        logging.error(f"Error in show_dashboard: {e}")
        return "Failed to retrieve dashboard", 500