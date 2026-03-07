# Epic Title: Banking Platform — Core API

from flask import Flask, jsonify, request
from backend.services.side_navigation_service import SideNavigationService
from backend.repositories.side_navigation_repository import SideNavigationRepository

app = Flask(__name__)

side_navigation_repository = SideNavigationRepository()
side_navigation_service = SideNavigationService(side_navigation_repository)

@app.route('/side_navigation', methods=['POST'])
def create_side_navigation():
    data = request.json
    side_navigation_service.create_side_navigation(name=data['name'], items=data['items'])
    return jsonify({"message": "Side Navigation created successfully"}), 201

@app.route('/side_navigation/<name>', methods=['GET'])
def get_side_navigation(name):
    side_navigation = side_navigation_service.get_side_navigation(name=name)
    if side_navigation:
        items = [{"name": item.name,
                  "url": item.url,
                  "category": item.category,
                  "sub_items": [{"name": sub.name, "url": sub.url} for sub in item.sub_items]
                 } for item in side_navigation.get_items()]
        return jsonify({
            "name": side_navigation.name,
            "items": items,
            "collapsed": side_navigation.is_collapsed()
        })
    return jsonify({"error": "Side Navigation not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)