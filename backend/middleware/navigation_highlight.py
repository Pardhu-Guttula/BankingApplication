# Epic Title: Banking Platform — Core API

from flask import request, jsonify
from backend.services.nav.navigation_service import NavigationService

def highlight_navigation_link(func):
    def wrapper(*args, **kwargs):
        link_id = request.args.get('link_id')
        service = NavigationService()
        state = service.update_navigation_state(highlighted_link_id=link_id, is_collapsed=False)
        return jsonify(state.__dict__), 200 if state.highlighted_link_id else 400
    return wrapper