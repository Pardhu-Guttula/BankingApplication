# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.header.header_service import HeaderService

header_bp = Blueprint('header_bp', __name__)

@header_bp.route('/header_features', methods=['GET'])
def get_header_features():
    service = HeaderService()
    features = service.get_features()
    return jsonify([feature.__dict__ for feature in features]), 200

@header_bp.route('/add_header_feature', methods=['POST'])
def add_header_feature():
    data = request.json
    service = HeaderService()
    feature = service.add_feature(
        feature_id=data['feature_id'],
        name=data['name']
    )
    return jsonify({"message": "Header feature added successfully", "feature_id": feature.feature_id}), 201