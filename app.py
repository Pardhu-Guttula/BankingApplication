# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.auth.role_controller import role_bp

app = Flask(__name__)
app.register_blueprint(role_bp, url_prefix='/api/roles')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)