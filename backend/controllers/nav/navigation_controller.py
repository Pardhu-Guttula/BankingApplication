# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.nav.navigation_service import NavigationService

navigation_bp = Blueprint('navigation_bp', __name__)

@navigation_bp.route('/navigation', methods=['GET'])
def get_navigation():
    service = NavigationService()
    navigation = service.get_navigation()
    return jsonify([menu_item.__dict__ for menu_item in navigation]), 200

@navigation_bp.route('/navigation/<item_id>', methods=['PUT'])
def update_menu_item(item_id):
    data = request.json
    name = data['name']
    route = data['route']
    highlighted = data['highlighted']
    service = NavigationService()
    service.update_menu_item(item_id, name, route, highlighted)
    return jsonify({"message": "Menu item updated successfully"}), 200

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 5: backend/controllers/nav/navigation_controller.py — SUCCESS.
Ledger updated: navigation_bp blueprint added | get_navigation() endpoint added | update_menu_item() endpoint added.
Epic Title comment verified: PRESENT.
Progress: 5 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 6: app.py
Responsibility: Application entry point, blueprint registration (Story 1).
Dependencies required: navigation_bp (memory-tracked: YES — emitted in File 5).
New exports to ledger: app instance.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 6: app.py