# Epic Title: Filter Products by Category

from flask import Flask
from backend.product_catalog.controllers.category_controller import category_bp
from backend.product_catalog.controllers.product_controller import product_bp

app = Flask(__name__)
app.register_blueprint(category_bp)
app.register_blueprint(product_bp)