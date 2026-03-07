# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.main_content.content_controller import content_bp

app = Flask(__name__)
app.register_blueprint(content_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)