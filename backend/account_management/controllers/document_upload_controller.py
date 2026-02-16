# Epic Title: Upload Documentation for Account Requests

import os
import logging
from werkzeug.utils import secure_filename
from flask import Blueprint, request, jsonify
from backend.account_management.services.document_upload_service import DocumentUploadService

# Controller for Document Uploads
document_upload_controller = Blueprint('document_upload_controller', __name__)
document_upload_service = DocumentUploadService()

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@document_upload_controller.route('/document/upload', methods=['POST'])
def upload_document():
    try:
        if 'file' not in request.files:
            return jsonify({"message": "No file part in the request"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(document_upload_service.upload_folder, filename)
            file.save(file_path)
            document_upload_service.save_document_metadata(filename, file_path)
            return jsonify({"message": "File uploaded successfully"}), 201
        else:
            return jsonify({"message": "File type not allowed"}), 400
    except Exception as e:
        logging.error(f"Error in upload_document: {e}")
        return jsonify({"message": "Document upload failed"}), 500