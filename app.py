# Epic Title: Banking Platform — Core API

from backend.services.main_content.service import MainContentService
from backend.repositories.main_content.repository import MainContentRepository
from backend.models.section import Section
from flask import Flask, jsonify
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

repository = MainContentRepository()
service = MainContentService(repository)

@app.route('/content/<section_name>', methods=['GET'])
def get_content(section_name: str):
    section = Section(name=section_name)
    content = service.get_main_content(section)
    information = service.get_section_information(section)
    return jsonify({
        "content": content.content,
        "information": {
            "title": information.title,
            "details": information.details
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)