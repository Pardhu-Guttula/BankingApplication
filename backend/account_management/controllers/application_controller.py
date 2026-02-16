# Epic Title: Save and Resume Incomplete Applications

import logging
from flask import Blueprint, request, jsonify
from backend.account_management.services.application_service import ApplicationService

# Controller for Managing Applications
application_controller = Blueprint('application_controller', __name__)
application_service = ApplicationService()

@application_controller.route('/application/save', methods=['POST'])
def save_application():
    try:
        data = request.json
        user_id = data.get("user_id")
        application_data = data.get("application_data")
        success = application_service.save_application(user_id, application_data)
        if success:
            return jsonify({"message": "Application saved successfully"}), 200
        return jsonify({"message": "Failed to save application"}), 400
    except Exception as e:
        logging.error(f"Error in save_application: {e}")
        return jsonify({"message": "Failed to save application"}), 500

@application_controller.route('/application/resume/<int:user_id>', methods=['GET'])
def resume_application(user_id):
    try:
        application_data = application_service.resume_application(user_id)
        if application_data:
            return jsonify(application_data), 200
        return jsonify({"message": "No application found to resume"}), 404
    except Exception as e:
        logging.error(f"Error in resume_application: {e}")
        return jsonify({"message": "Failed to resume application"}), 500