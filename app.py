# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.monitoring_controller import monitoring_bp

app = Flask(__name__)
app.register_blueprint(monitoring_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)