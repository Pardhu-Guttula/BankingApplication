# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.nav.navigation_service import NavigationService

nav_bp = Blueprint('nav_bp', __name__)

@nav_bp.route('/navigation_links', methods=['GET'])
def get_navigation_links():
    service = NavigationService()
    links = service.get_navigation_links()
    return jsonify([link.__dict__ for link in links]), 200

@nav_bp.route('/navigation_state', methods=['POST'])
def update_navigation_state():
    data = request.json
    service = NavigationService()
    state = service.update_navigation_state(
        highlighted_link_id=data['highlighted_link_id'],
        is_collapsed=data['is_collapsed']
    )
    return jsonify(state.__dict__), 200