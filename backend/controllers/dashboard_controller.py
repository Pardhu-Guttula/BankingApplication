# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.dashboard_service import DashboardService

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard', methods=['GET'])
def get_dashboard():
    service = DashboardService()
    dashboard = service.get_dashboard()
    return jsonify({
        "main_content": {"views": [{"name": view.name, "content": view.content} for view in dashboard.main_content.get_views()]},
        "side_navigation": {"items": [{"name": item.name, "url": item.url} for item in dashboard.side_navigation.get_items()]},
        "header": {"title": dashboard.header.title, "links": [{"name": link.name, "url": link.url} for link in dashboard.header.get_links()]}
    })

@dashboard_bp.route('/dashboard', methods=['POST'])
def create_dashboard():
    data = request.json
    main_content_data = data['main_content']
    side_navigation_data = data['side_navigation']
    header_data = data['header']
    # Assuming services to instantiate the components
    service = DashboardService()
    dashboard = service.create_dashboard(main_content_data, side_navigation_data, header_data)
    return jsonify({"message": "Dashboard created successfully"}), 201