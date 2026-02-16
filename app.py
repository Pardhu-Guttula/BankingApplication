# Epic Title: Intuitive Dashboard Interface

import logging
from flask import Flask
from backend.database import db
from backend.personalized_dashboard.controllers.ui_controller import ui_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(ui_controller, url_prefix='/ui')

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)