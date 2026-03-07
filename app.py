# Epic Title: Banking Platform — Core API

from flask import Flask, jsonify, request
from backend.services.main_content_service import MainContentService
from backend.repositories.main_content_repository import MainContentRepository

app = Flask(__name__)

main_content_repository = MainContentRepository()
main_content_service = MainContentService(main_content_repository)

@app.route('/main_content_area', methods=['POST'])
def create_main_content_area():
    data = request.json
    main_content_service.create_main_content_area(views=data['views'])
    return jsonify({"message": "Main Content Area created successfully"}), 201

@app.route('/main_content_area', methods=['GET'])
def get_main_content_area():
    main_content_area = main_content_service.get_main_content_area()
    if main_content_area:
        views = [{"name": view.name, "content": view.content} for view in main_content_area.get_views()]
        current_view = main_content_area.get_current_view()
        return jsonify({
            "views": views,
            "current_view": {"name": current_view.name, "content": current_view.content} if current_view else None
        })
    return jsonify({"error": "Main Content Area not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)