# Epic Title: Banking Platform — Core API

from flask import Flask, jsonify, request
from backend.services.layout_service import LayoutService
from backend.repositories.layout_repository import LayoutRepository

app = Flask(__name__)

layout_repository = LayoutRepository()
layout_service = LayoutService(layout_repository)

@app.route('/layout', methods=['POST'])
def create_layout():
    data = request.json
    layout_service.create_layout(name=data['name'], components=data['components'])
    return jsonify({"message": "Layout created successfully"}), 201

@app.route('/layout/<name>', methods=['GET'])
def get_layout(name):
    layout = layout_service.get_layout(name=name)
    if layout:
        return jsonify({
            "name": layout.name,
            "components": layout.components
        })
    return jsonify({"error": "Layout not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)