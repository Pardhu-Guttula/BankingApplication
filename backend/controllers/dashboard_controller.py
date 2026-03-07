# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.dashboard.realtime_data_service import RealTimeDataService

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/realtime_data', methods=['POST'])
def update_realtime_data():
    data = request.json
    service = RealTimeDataService()
    realtime_data = service.update_realtime_data(data_id=data['data_id'], content=data['content'])
    return jsonify({"message": "Real-time data updated successfully", "content": realtime_data.content}), 201

@dashboard_bp.route('/realtime_data', methods=['GET'])
def get_latest_data():
    service = RealTimeDataService()
    realtime_data = service.get_latest_data()
    if realtime_data:
        return jsonify({"content": realtime_data.content, "timestamp": realtime_data.timestamp})
    else:
        return jsonify({"message": "No real-time data available"}), 404