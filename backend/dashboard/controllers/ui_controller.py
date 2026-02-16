# Epic Title: Ensure Intuitive Dashboard Interface

from flask import Blueprint, jsonify

ui_controller = Blueprint('ui_controller', __name__)

@ui_controller.route('/dashboard/ui', methods=['GET'])
def get_dashboard_ui():
    ui_structure = {
        'navigation': [
            {'name': 'Home', 'link': '/dashboard'},
            {'name': 'Profile', 'link': '/profile'},
            {'name': 'Settings', 'link': '/settings'},
            {'name': 'Logout', 'link': '/logout'}
        ],
        'sections': [
            {'name': 'Overview', 'id': 'overview-section'},
            {'name': 'Accounts', 'id': 'accounts-section'},
            {'name': 'Transactions', 'id': 'transactions-section'},
            {'name': 'Support', 'id': 'support-section'}
        ]
    }
    return jsonify(ui_structure), 200