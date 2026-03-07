# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.nav.navigation_controller import nav_bp

app = Flask(__name__)
app.register_blueprint(nav_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)