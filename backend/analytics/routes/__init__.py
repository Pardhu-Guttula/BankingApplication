# Epic Title: Track sales performance metrics

from flask import Flask
from backend.analytics.controllers.sales_controller import sales_bp

app = Flask(__name__)
app.register_blueprint(sales_bp)