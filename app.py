# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.service_modifications.modification_request_controller import modification_request_bp

app = Flask(__name__)
app.register_blueprint(modification_request_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)