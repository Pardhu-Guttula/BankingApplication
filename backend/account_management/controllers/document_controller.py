# Epic Title: Upload Documentation for Account Requests

import logging
import os
from flask import Blueprint, request, jsonify
from backend.account_management.services.document_service import DocumentService

# Configuration for allowed document types
ALLOWED_EXTENSIONS = {'pdf', 'jpeg', 'jpg', 'png'}
UPLOAD_FOLDER = 'backend/account_management/static/uploads'

# Controller for Document Management
document_controller = Blueprint('document_controller', __name__)
document_service = DocumentService()


def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@document_controller.route('/document/upload', methods=['POST'])
def upload_document():
    try:
        if 'document' not in request.files:
            return jsonify({"message": "No document part"}), 400

        file = request.files['document']
        user_id = request.form['user_id']

        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400

        if file and allowed_file(file.filename):
            filename = document_service.save_document(file, user_id, UPLOAD_FOLDER)
            return jsonify({"message": "Document uploaded successfully", "filename": filename}), 201
        else:
            return jsonify({"message": "Unsupported file format"}), 400
    except Exception as e:
        logging.error(f'Error in upload_document: {e}')
        return jsonify({"message": "Document upload failed"}), 500