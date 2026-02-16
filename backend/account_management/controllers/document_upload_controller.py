# Epic Title: Upload Documentation for Account Requests

import logging
import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from backend.account_management.services.document_upload_service import DocumentUploadService

# Controller for Document Uploads
document_upload_controller = Blueprint('document_upload_controller', __name__)
document_upload_service = DocumentUploadService()

UPLOAD_FOLDER = '/path/to/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@document_upload_controller.route('/document/upload', methods=['POST'])
def upload_document():
    try:
        if 'file' not in request.files:
            return jsonify({"message": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            document_upload_service.save_document_info(request.form['user_id'], filename)
            return jsonify({"message": "File uploaded successfully"}), 200
        return jsonify({"message": "File type not allowed"}), 400
    except Exception as e:
        logging.error(f"Error in upload_document: {e}")
        return jsonify({"message": "Failed to upload document"}), 500