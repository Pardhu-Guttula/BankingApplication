# Epic Title: Change Password

from flask import Flask
from backend.user_profile.controllers.password_controller import password_bp

app = Flask(__name__)
app.register_blueprint(password_bp)