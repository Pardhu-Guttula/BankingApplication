# Epic Title: User-Friendly Account Service Interface

from flask import Blueprint, request, jsonify

account_modification_controller = Blueprint('account_modification_controller', __name__)

@account_modification_controller.route('/account/modification/navigation', methods=['GET'])
def get_modification_navigation():
    navigation_options = {
        'sections': [
            {
                'name': 'Manage Services',
                'actions': [
                    {'name': 'Update Account Details', 'link': '/account/update_details'},
                    {'name': 'Request Account Closure', 'link': '/account/request_closure'}
                ]
            },
            {
                'name': 'Modify Preferences',
                'actions': [
                    {'name': 'Change Notification Settings', 'link': '/account/change_notifications'},
                    {'name': 'Update Security Settings', 'link': '/account/update_security'}
                ]
            },
            {
                'name': 'Account History',
                'actions': [
                    {'name': 'View Transaction History', 'link': '/account/transaction_history'},
                    {'name': 'Download Statements', 'link': '/account/download_statements'}
                ]
            }
        ]
    }
    return jsonify(navigation_options), 200