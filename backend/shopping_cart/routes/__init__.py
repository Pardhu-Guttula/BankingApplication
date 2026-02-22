# Epic Title: Update product quantities in the shopping cart

from flask import Flask
from backend.shopping_cart.controllers.shopping_cart_controller import shopping_cart_bp

app = Flask(__name__)
app.register_blueprint(shopping_cart_bp)