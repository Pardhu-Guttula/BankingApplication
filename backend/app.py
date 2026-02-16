# Epic Title: Implement Data Encryption Protocols

import logging
from flask import Flask
from backend.core_banking.controllers.encryption_controller import encryption_controller
from backend.core_banking.models.encrypted_data_model import db as core_banking_db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    core_banking_db.init_app(app)
    app.register_blueprint(encryption_controller)

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)