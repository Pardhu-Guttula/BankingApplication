# Epic Title: Filter Products by Category

import logging
from flask import Flask
from backend.product_catalog.routes import app as product_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(product_app)
    
    @app.route('/')
    def home():
        return 'Welcome to the Product Catalog!'
    
    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)