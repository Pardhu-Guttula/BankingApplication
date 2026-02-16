# Epic Title: Intuitive Dashboard Interface

import logging
from flask import Blueprint, render_template

# Controller for User Interface
ui_controller = Blueprint('ui_controller', __name__)

@ui_controller.route('/dashboard', methods=['GET'])
def dashboard():
    try:
        # Render the user-friendly dashboard template
        return render_template('dashboard.html')
    except Exception as e:
        logging.error(f"Error in rendering dashboard: {e}")
        return "Failed to load dashboard", 500