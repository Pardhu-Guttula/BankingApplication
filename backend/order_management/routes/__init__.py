# Epic Title: View Order History

from flask import Flask
from backend.order_management.controllers.order_controller import order_bp

app = Flask(__name__)
app.register_blueprint(order_bp)