# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.dashboard.dashboard_service import DashboardService

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/widgets', methods=['GET'])
def get_all_widgets():
    service = DashboardService()
    widgets = service.get_all_widgets()
    return jsonify([widget.__dict__ for widget in widgets]), 200

@dashboard_bp.route('/widgets/<widget_id>', methods=['GET'])
def get_widget_by_id(widget_id):
    service = DashboardService()
    widget = service.get_widget_by_id(widget_id)
    return jsonify(widget.__dict__), 200

### Checkpoint 5 — Post-Emission: Each File

Post-emit File 5: backend/controllers/dashboard/dashboard_controller.py — SUCCESS.
Ledger updated: dashboard_bp blueprint added | get_all_widgets() endpoint added | get_widget_by_id() endpoint added.
Epic Title comment verified: PRESENT.
Progress: 5 of 7 files emitted.

### Checkpoint 4 — Pre-Emission: Each File

Pre-emit File 6: app.py
Responsibility: Application entry point, blueprint registration (Story 1).
Dependencies required: dashboard_bp (memory-tracked: YES — emitted in File 5).
New exports to ledger: app instance.
Epic Title comment: will be injected at line 1.
Proceeding to emit.

### Emitting File 6: app.py