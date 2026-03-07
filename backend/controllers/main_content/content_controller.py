# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.main_content.content_service import ContentService

content_bp = Blueprint('content_bp', __name__)

@content_bp.route('/content_elements', methods=['GET'])
def get_content_elements():
    service = ContentService()
    elements = service.get_content_elements()
    return jsonify([element.__dict__ for element in elements]), 200

@content_bp.route('/add_content_element', methods=['POST'])
def add_content_element():
    data = request.json
    service = ContentService()
    content_element = service.add_content_element(
        element_id=data['element_id'],
        content=data['content']
    )
    return jsonify({"message": "Content element added successfully", "element_id": content_element.element_id}), 201