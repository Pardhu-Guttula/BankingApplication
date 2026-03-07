# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.main_content.content_service import ContentService

content_bp = Blueprint('content_bp', __name__)

@content_bp.route('/add_content', methods=['POST'])
def add_content():
    data = request.json
    service = ContentService()
    content_element = service.add_content_element(
        element_id=data['element_id'],
        content=data['content']
    )
    return jsonify({"message": "Content element added successfully", "element_id": content_element.element_id}), 201