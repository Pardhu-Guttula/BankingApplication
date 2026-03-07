# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.header.header_service import HeaderService

header_bp = Blueprint('header_bp', __name__)

@header_bp.route('/header_elements', methods=['GET'])
def get_header_elements():
    service = HeaderService()
    elements = service.get_header_elements()
    return jsonify([element.__dict__ for element in elements]), 200

@header_bp.route('/add_header_element', methods=['POST'])
def add_header_element():
    data = request.json
    service = HeaderService()
    header_element = service.add_header_element(
        element_id=data['element_id'],
        content=data['content']
    )
    return jsonify({"message": "Header element added successfully", "element_id": header_element.element_id}), 201