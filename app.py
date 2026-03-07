# Epic Title: Banking Platform — Core API

from flask import Flask
from backend.controllers.account_opening.account_controller import account_opening_bp

app = Flask(__name__)
app.register_blueprint(account_opening_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)