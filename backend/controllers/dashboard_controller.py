# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.dashboard.service import Service

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/add_service', methods=['POST'])
def add_service():
    data = request.json
    service = Service()
    service_data = service.add_banking_service(data['service_id'], data['name'], data['description'], data['eligibility_criteria'])
    return jsonify({"message": "Banking service added successfully"}), 201

@dashboard_bp.route('/services', methods=['GET'])
def get_all_services():
    service = Service()
    services = service.get_all_services()
    return jsonify([{
        "service_id": service.service_id,
        "name": service.name,
        "description": service.description,
        "eligibility_criteria": service.eligibility_criteria
    } for service in services])

@dashboard_bp.route('/eligible_services', methods=['GET'])
def get_eligible_services():
    eligibility_criteria = request.args.get('eligibility_criteria')
    service = Service()
    services = service.get_eligible_services(eligibility_criteria)
    return jsonify([{
        "service_id": service.service_id,
        "name": service.name,
        "description": service.description,
        "eligibility_criteria": service.eligibility_criteria
    } for service in services])

@dashboard_bp.route('/service_details/<service_id>', methods=['GET'])
def get_service_details(service_id):
    service = Service()
    service_data = service.get_service_details(service_id)
    if service_data:
        return jsonify({
            "service_id": service_data.service_id,
            "name": service_data.name,
            "description": service_data.description,
            "eligibility_criteria": service_data.eligibility_criteria
        })
    else:
        return jsonify({"message": "Service not found"}), 404