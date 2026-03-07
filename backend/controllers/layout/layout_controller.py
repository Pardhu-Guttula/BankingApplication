# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.layout.layout_service import LayoutService

layout_bp = Blueprint('layout_bp', __name__)

@layout_bp.route('/layout', methods=['GET'])
def get_layout():
    layout_id = request.args.get('layout_id')
    service = LayoutService()
    layout = service.get_layout(layout_id)
    return jsonify(layout.__dict__), 200

@layout_bp.route('/add_layout', methods=['POST'])
def add_layout():
    data = request.json
    service = LayoutService()
    layout = service.add_layout(
        layout_id=data['layout_id'],
        screen_size=data['screen_size'],
        breakpoint=data['breakpoint']
    )
    return jsonify({"message": "Layout added successfully", "layout_id": layout.layout_id}), 201