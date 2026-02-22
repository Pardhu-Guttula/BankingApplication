# Epic Title: Integrate payment gateway (Stripe) for processing payments

import logging
from flask import Flask
from backend.payment.routes import app as payment_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(payment_app)
    
    @app.route('/')
    def home():
        return 'Welcome to the Payment Gateway!'
    
    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)