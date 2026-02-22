# Epic Title: Update Personal Information

from flask import Flask
from backend.user_profile.controllers.profile_controller import profile_bp

app = Flask(__name__)
app.register_blueprint(profile_bp)