# Epic Title: Banking Platform — Core API

from flask import request, jsonify
from backend.services.layout.layout_service import LayoutService

def handle_responsiveness(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        layout_service = LayoutService()
        device_type = request.user_agent.platform
        layout_service.adapt_layout(device_type)
        # Factor in specific breakpoint logic for content rendering
        return response
    return wrapper