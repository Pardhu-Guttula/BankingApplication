# Epic Title: User-Friendly Account Service Interface

import logging
from flask import Flask
from backend.account_requests.controllers.account_opening_controller import account_opening_controller
from backend.account_requests.controllers.service_modification_controller import service_modification_controller
from backend.account_requests.controllers.modification_ui_controller import modification_ui_controller
from backend.account_requests.models.account_request_model import db as account_db
from backend.account_requests.models.service_modification_model import db as modification_db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    account_db.init_app(app)
    modification_db.init_app(app)
    
    app.register_blueprint(account_opening_controller)
    app.register_blueprint(service_modification_controller)
    app.register_blueprint(modification_ui_controller)
    
    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)