# Epic Title: Manage Account

from flask import Flask
from backend.account_management.controllers.account_controller import account_bp

app = Flask(__name__)
app.register_blueprint(account_bp)