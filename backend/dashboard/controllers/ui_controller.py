# Epic Title: Ensure Intuitive Dashboard Interface

from flask import Blueprint, jsonify

ui_controller = Blueprint('ui_controller', __name__)

@ui_controller.route('/dashboard/navigation', methods=['GET'])
def get_navigation_options():
    navigation_options = [
        {'name': 'Account Summary', 'link': '/dashboard/account_summary'},
        {'name': 'Transfer Funds', 'link': '/dashboard/transfer_funds'},
        {'name': 'View Statements', 'link': '/dashboard/view_statements'},
        {'name': 'Manage Profile', 'link': '/dashboard/manage_profile'},
        {'name': 'Customer Support', 'link': '/dashboard/customer_support'}
    ]
    return jsonify(navigation_options), 200