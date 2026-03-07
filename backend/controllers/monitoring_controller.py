# Epic Title: Banking Platform — Core API

from flask import Blueprint, request, jsonify
from backend.services.monitoring_service import MonitoringService

monitoring_bp = Blueprint('monitoring_bp', __name__)

@monitoring_bp.route('/alerts', methods=['POST'])
def create_alert():
    data = request.json
    service = MonitoringService()
    service.generate_alert(data['alert'])
    return jsonify({"message": "Alert generated successfully"}), 201

@monitoring_bp.route('/alerts', methods=['GET'])
def get_alerts():
    service = MonitoringService()
    alerts = service.get_all_alerts()
    return jsonify(alerts)

@monitoring_bp.route('/performance_reports', methods=['POST'])
def create_performance_report():
    data = request.json
    service = MonitoringService()
    service.generate_performance_report(data['report'])
    return jsonify({"message": "Performance report generated successfully"}), 201

@monitoring_bp.route('/performance_reports', methods=['GET'])
def get_performance_reports():
    service = MonitoringService()
    reports = service.get_all_performance_reports()
    return jsonify(reports)