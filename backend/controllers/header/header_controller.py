# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.header.header_service import HeaderService

header_bp = Blueprint('header_bp', __name__)

@header_bp.route('/navigation-links', methods=['GET'])
def get_navigation_links():
    service = HeaderService()
    links = service.get_navigation_links()
    return jsonify([link.__dict__ for link in links]), 200

@header_bp.route('/navigation-link/<link_id>', methods=['PUT'])
def update_navigation_link(link_id):
    data = request.json
    name = data['name']
    route = data['route']
    key_functionality = data['key_functionality']
    service = HeaderService()
    service.update_navigation_link(link_id, name, route, key_functionality)
    return jsonify({"message": "Navigation link updated successfully"}), 200