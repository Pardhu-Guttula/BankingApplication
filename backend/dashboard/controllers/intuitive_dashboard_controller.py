# Epic Title: Ensure Intuitive Dashboard Interface

from flask import Blueprint, jsonify

intuitive_dashboard_controller = Blueprint('intuitive_dashboard_controller', __name__)

@intuitive_dashboard_controller.route('/dashboard/ui', methods=['GET'])
def get_dashboard_ui():
    ui_structure = {
        'navigation': [
            {'name': 'Account Overview', 'link': '/dashboard/account'},
            {'name': 'Transactions', 'link': '/dashboard/transactions'},
            {'name': 'Settings', 'link': '/dashboard/settings'},
        ],
        'key_functions': [
            {'name': 'Transfer Money', 'id': 'transfer-money'},
            {'name': 'Pay Bills', 'id': 'pay-bills'},
            {'name': 'Customer Support', 'id': 'customer-support'},
        ]
    }
    return jsonify(ui_structure), 200