# Epic Title: User-Friendly Account Service Interface

from flask import Blueprint, jsonify

account_service_interface_controller = Blueprint('account_service_interface_controller', __name__)

@account_service_interface_controller.route('/account_services/ui', methods=['GET'])
def get_account_service_ui():
    ui_structure = {
        'navigation': [
            {'name': 'Overview', 'link': '/account_services/overview'},
            {'name': 'Modify Account', 'link': '/account_services/modify'},
            {'name': 'Close Account', 'link': '/account_services/close'},
        ],
        'modification_options': [
            {'name': 'Change Address', 'id': 'change-address'},
            {'name': 'Update Contact Details', 'id': 'update-contact'},
            {'name': 'Upgrade Account Type', 'id': 'upgrade-account'},
        ],
        'status': [
            {'name': 'Pending Requests', 'link': '/account_services/status/pending'},
            {'name': 'Completed Requests', 'link': '/account_services/status/completed'},
        ]
    }
    return jsonify(ui_structure), 200