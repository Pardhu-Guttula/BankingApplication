# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.account_opening.request_controller import request_bp

app = Flask(__name__)
app.register_blueprint(request_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)