# Epic Title: Design User Profile-Based Dashboard

import logging
from flask import Flask
from backend.dashboard.controllers.dashboard_controller import dashboard_controller
from backend.dashboard.models.user_profile_model import db as dashboard_db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    dashboard_db.init_app(app)

    app.register_blueprint(dashboard_controller)

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)