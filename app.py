# Epic Title: Integrate Authentication with Bank Security Infrastructure

import logging
from flask import Flask
from backend.database import db
from backend.user_authentication.controllers.security_integration_controller import security_integration_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(security_integration_controller, url_prefix='/security')

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)