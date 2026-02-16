# Epic Title: User-Friendly Account Service Interface

import logging
from flask import Flask
from backend.account_requests.controllers.account_service_interface_controller import account_service_interface_controller
from backend.account_requests.models.service_modification_request_model import db as service_modification_db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    service_modification_db.init_app(app)

    app.register_blueprint(account_service_interface_controller)

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)