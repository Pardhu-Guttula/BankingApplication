# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.nav.menu_service import MenuService

menu_bp = Blueprint('menu_bp', __name__)

@menu_bp.route('/menu_items', methods=['GET'])
def get_menu_items():
    user_role = request.args.get('role')
    service = MenuService()
    items = service.get_menu_items(user_role)
    return jsonify([item.__dict__ for item in items]), 200

@menu_bp.route('/add_menu_item', methods=['POST'])
def add_menu_item():
    data = request.json
    service = MenuService()
    menu_item = service.add_menu_item(
        item_id=data['item_id'],
        name=data['name'],
        role=data['role']
    )
    return jsonify({"message": "Menu item added successfully", "item_id": menu_item.item_id}), 201