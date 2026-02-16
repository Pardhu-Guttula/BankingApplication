# Epic Title: Intuitive Dashboard Interface

import logging
from flask import Blueprint, render_template

# Controller for rendering the UI of Personalized Dashboard
dashboard_ui_controller = Blueprint('dashboard_ui_controller', __name__)

@dashboard_ui_controller.route('/dashboard_ui/<int:user_id>', methods=['GET'])
def render_dashboard_ui(user_id: int):
    try:
        # Render HTML template for the dashboard
        return render_template('dashboard.html', user_id=user_id), 200
    except Exception as e:
        logging.error(f'Error in render_dashboard_ui: {e}')
        return "Failed to load dashboard UI", 500