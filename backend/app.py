# Epic Title: Implement Multi-Factor Authentication

import logging
from flask import Flask
from backend.authentication.controllers.mfa_controller import mfa_controller
from backend.authentication.models.mfa_model import db as mfa_db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    mfa_db.init_app(app)

    app.register_blueprint(mfa_controller)

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)