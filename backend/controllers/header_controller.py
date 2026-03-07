# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.header.header_service import HeaderService
from backend.models.header.header_menu import HeaderLink

header_bp = Blueprint('header_bp', __name__)

@header_bp.route('/header_menu', methods=['POST'])
def create_header_menu():
    data = request.json
    service = HeaderService()
    service.create_header_menu(title=data['title'], links=data['links'])
    return jsonify({"message": "Header Menu created successfully"}), 201

@header_bp.route('/header_menu', methods=['GET'])
def get_header_menu():
    service = HeaderService()
    header_menu = service.get_header_menu()
    links = [{"name": link.name, "url": link.url} for link in header_menu.get_links()]
    return jsonify({
        "title": header_menu.title,
        "links": links
    })