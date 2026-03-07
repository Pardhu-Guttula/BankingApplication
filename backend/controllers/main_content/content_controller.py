# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.main_content.content_service import ContentService

content_bp = Blueprint('content_bp', __name__)

@content_bp.route('/content', methods=['GET'])
def get_content():
    content_id = request.args.get('content_id')
    service = ContentService()
    content = service.get_content(content_id)
    return jsonify(content.__dict__), 200

@content_bp.route('/add_content', methods=['POST'])
def add_content():
    data = request.json
    service = ContentService()
    content = service.add_content(
        content_id=data['content_id'],
        title=data['title'],
        body=data['body']
    )
    return jsonify({"message": "Content added successfully", "content_id": content.content_id}), 201