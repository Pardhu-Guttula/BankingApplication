# Epic Title: Integrate Authentication with Bank Security Infrastructure

import logging
from flask import Blueprint, request, jsonify
from backend.authentication.services.auth_integration_service import AuthIntegrationService

# Controller for Authentication Integration
auth_integration_controller = Blueprint('auth_integration_controller', __name__)
auth_integration_service = AuthIntegrationService()

@auth_integration_controller.route('/auth/integrate', methods=['POST'])
def integrate_auth_system():
    try:
        data = request.json
        integration_details = data.get("integration_details")
        if auth_integration_service.integrate_with_security_system(integration_details):
            return jsonify({"message": "Authentication system integrated successfully"}), 200
        return jsonify({"message": "Failed to integrate authentication system"}), 400
    except Exception as e:
        logging.error(f"Error in integrate_auth_system: {e}")
        return jsonify({"message": "Integration failed"}), 500