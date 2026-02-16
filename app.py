# Epic Title: Upload Documentation for Account Requests

import logging
from flask import Flask
from backend.database import db
from backend.account_management.controllers.document_upload_controller import document_upload_controller

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/dbname'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = '/path/to/upload/folder'

    db.init_app(app)
    app.register_blueprint(document_upload_controller, url_prefix='/document')

    return app

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(host='0.0.0.0', port=5000)