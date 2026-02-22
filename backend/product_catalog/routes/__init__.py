# Epic Title: Sort Products by Price

from flask import Flask
from backend.product_catalog.controllers.product_controller import product_bp

app = Flask(__name__)
app.register_blueprint(product_bp)