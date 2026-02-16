# Epic Title: Implement Account Lockout Mechanism

import logging
from flask import Flask
from backend.authentication.controllers.login_attempt_controller import login_attempt_controller
from backend.authentication.models.failed_login_attempt_model import db as login_db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_db.init_app(app)

    app.register_blueprint(login_attempt_controller)

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)