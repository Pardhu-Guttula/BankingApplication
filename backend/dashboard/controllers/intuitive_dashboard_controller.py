# Epic Title: Ensure Intuitive Dashboard Interface

from flask import Blueprint, jsonify

intuitive_dashboard_controller = Blueprint('intuitive_dashboard_controller', __name__)

@intuitive_dashboard_controller.route('/dashboard/navigation', methods=['GET'])
def get_dashboard_navigation():
    navigation_structure = {
        'sections': [
            {
                'name': 'Overview',
                'actions': [
                    {'name': 'View Account Balance', 'link': '/dashboard/account_balance'},
                    {'name': 'Recent Transactions', 'link': '/dashboard/recent_transactions'}
                ]
            },
            {
                'name': 'Manage Accounts',
                'actions': [
                    {'name': 'Open New Account', 'link': '/dashboard/open_account'},
                    {'name': 'Close Account', 'link': '/dashboard/close_account'}
                ]
            },
            {
                'name': 'Settings',
                'actions': [
                    {'name': 'Profile Settings', 'link': '/dashboard/profile_settings'},
                    {'name': 'Security Settings', 'link': '/dashboard/security_settings'}
                ]
            }
        ]
    }
    return jsonify(navigation_structure), 200