# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.auth.session_controller import session_bp
from backend.middleware.session_expiration import session_expiration_middleware

app = Flask(__name__)
app.register_blueprint(session_bp, url_prefix='/api')
session_expiration_middleware(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)