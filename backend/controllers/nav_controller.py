# Epic Title: Banking Platform — Core API

from flask import Blueprint, jsonify, request
from backend.services.nav.navigation_service import NavigationService
from backend.models.nav.navigation_menu import NavigationLink

nav_bp = Blueprint('nav_bp', __name__)

@nav_bp.route('/navigation_menu', methods=['POST'])
def create_navigation_menu():
    data = request.json
    service = NavigationService()
    service.create_navigation_menu(links=data['links'])
    return jsonify({"message": "Navigation Menu created successfully"}), 201

@nav_bp.route('/navigation_menu', methods=['GET'])
def get_navigation_menu():
    service = NavigationService()
    navigation_menu = service.get_navigation_menu()
    links = [{"name": link.name, "url": link.url, "icon": link.icon} for link in navigation_menu.get_links()]
    active_link = navigation_menu.get_active_link()
    return jsonify({
        "expanded": navigation_menu.expanded,
        "links": links,
        "active_link": {"name": active_link.name, "url": active_link.url, "icon": active_link.icon} if active_link else None
    })

@nav_bp.route('/navigation_menu/toggle', methods=['POST'])
def toggle_navigation_menu():
    service = NavigationService()
    service.toggle_navigation_menu()
    return jsonify({"message": "Navigation Menu toggled successfully"}), 200

@nav_bp.route('/navigation_menu/active_link', methods=['POST'])
def set_active_link():
    data = request.json
    service = NavigationService()
    active_link = NavigationLink(name=data['name'], url=data['url'], icon=data['icon'])
    service.set_active_link(active_link)
    return jsonify({"message": "Active link set successfully"}), 200