# Epic Title: Simplify Account Opening Workflow

import logging
from flask import Flask
from backend.account_requests.controllers.account_request_controller import account_request_controller
from backend.account_requests.models.account_request_model import db as account_request_db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    account_request_db.init_app(app)

    app.register_blueprint(account_request_controller)

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)