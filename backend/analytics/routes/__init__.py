# Epic Title: Monitor user behavior metrics

from flask import Flask
from backend.analytics.controllers.user_behavior_controller import behavior_bp

app = Flask(__name__)
app.register_blueprint(behavior_bp)