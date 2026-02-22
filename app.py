# Epic Title: Display order confirmation to customers after successful payment

import logging
from flask import Flask
from backend.order_management.routes import app as order_management_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(order_management_app)
    
    @app.route('/')
    def home():
        return 'Welcome to the Order Management System!'
    
    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)