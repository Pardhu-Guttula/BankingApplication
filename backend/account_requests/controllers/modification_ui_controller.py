# Epic Title: User-Friendly Account Service Interface

from flask import Blueprint, jsonify

modification_ui_controller = Blueprint('modification_ui_controller', __name__)

@modification_ui_controller.route('/modification/ui', methods=['GET'])
def get_modification_ui():
    ui_structure = {
        'navigation': [
            {'name': 'Open Account', 'link': '/account/open'},
            {'name': 'Modify Account', 'link': '/service/modify'},
            {'name': 'View Status', 'link': '/status/view'},
        ],
        'modification_options': [
            {'name': 'Change Address', 'id': 'change-address'},
            {'name': 'Update Contact Info', 'id': 'update-contact-info'},
            {'name': 'Upgrade Account', 'id': 'upgrade-account'},
        ]
    }
    return jsonify(ui_structure), 200