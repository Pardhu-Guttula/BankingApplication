# Epic Title: Display reviews on product detail pages

import logging
from flask import Flask
from backend.reviews.routes import app as reviews_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(reviews_app)
    
    @app.route('/')
    def home():
        return 'Welcome to the Product Review Display System!'
    
    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)