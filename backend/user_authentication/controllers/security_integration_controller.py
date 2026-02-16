# Epic Title: Integrate Authentication with Bank Security Infrastructure

import logging
from flask import Blueprint, request, jsonify
from backend.user_authentication.services.security_integration_service import SecurityIntegrationService

# Controller for integration with Bank Security Infrastructure
security_integration_controller = Blueprint('security_integration_controller', __name__)
security_integration_service = SecurityIntegrationService()

@security_integration_controller.route('/security/integrate', methods=['POST'])
def integrate_security_system():
    try:
        data = request.json
        integration_data = data.get("integration_data")
        integration_success = security_integration_service.integrate_with_bank(integration_data)
        if integration_success:
            return jsonify({"message": "Integration successful"}), 200
        return jsonify({"message": "Integration failed"}), 400
    except Exception as e:
        logging.error(f"Error in integrate_security_system: {e}")
        return jsonify({"message": "Integration failed"}), 500