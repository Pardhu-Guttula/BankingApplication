# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.dashboard.dashboard_service import DashboardService

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
def get_dashboard():
    dashboard_id = request.args.get('dashboard_id')
    service = DashboardService()
    dashboard = service.get_dashboard(dashboard_id)
    return jsonify(dashboard.__dict__), 200

@dashboard_bp.route('/add_dashboard', methods=['POST'])
def add_dashboard():
    data = request.json
    service = DashboardService()
    dashboard = service.add_dashboard(
        dashboard_id=data['dashboard_id'],
        name=data['name']
    )
    return jsonify({"message": "Dashboard added successfully", "dashboard_id": dashboard.dashboard_id}), 201