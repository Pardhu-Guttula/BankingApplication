# Epic Title: Banking Platform — Core API

from flask import Flask, jsonify, request
from backend.services.header_service import HeaderService
from backend.repositories.header_repository import HeaderRepository

app = Flask(__name__)

header_repository = HeaderRepository()
header_service = HeaderService(header_repository)

@app.route('/header', methods=['POST'])
def create_header():
    data = request.json
    header_service.create_header(title=data['title'], links=data['links'])
    return jsonify({"message": "Header created successfully"}), 201

@app.route('/header/<title>', methods=['GET'])
def get_header(title):
    header = header_service.get_header(title=title)
    if header:
        links = [{"name": link.name, "url": link.url} for link in header.get_links()]
        return jsonify({
            "title": header.title,
            "links": links
        })
    return jsonify({"error": "Header not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)