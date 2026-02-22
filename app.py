# Epic Title: Remove products from the shopping cart

import logging
from flask import Flask
from backend.shopping_cart.routes import app as shopping_cart_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(shopping_cart_app)
    
    @app.route('/')
    def home():
        return 'Welcome to the Shopping Cart!'
    
    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)