# Epic Title: Generate detailed e-commerce performance reports

from flask import Flask
from backend.analytics_reporting.controllers.performance_controller import performance_bp

app = Flask(__name__)
app.register_blueprint(performance_bp)