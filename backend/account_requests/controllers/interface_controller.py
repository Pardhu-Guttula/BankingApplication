# Epic Title: User-Friendly Account Service Interface

from flask import Blueprint, jsonify

interface_controller = Blueprint('interface_controller', __name__)

@interface_controller.route('/account/modification-options', methods=['GET'])
def get_modification_options():
    modification_options = [
        {'name': 'Change Account Type', 'link': '/account/modify/type'},
        {'name': 'Update Contact Information', 'link': '/account/modify/contact'},
        {'name': 'Add Account Holder', 'link': '/account/modify/add_holder'},
        {'name': 'Close Account', 'link': '/account/modify/close'}
    ]
    return jsonify(modification_options), 200