# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.nav_controller import nav_bp
from backend.controllers.header_controller import header_bp

app = Flask(__name__)
app.register_blueprint(nav_bp, url_prefix='/api')
app.register_blueprint(header_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)