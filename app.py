# Epic Title: Generate detailed e-commerce performance reports

import logging
from flask import Flask
from backend.analytics_reporting.routes import app as analytics_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(analytics_app)
    
    @app.route('/')
    def home():
        return 'Welcome to the E-commerce Performance Reporting System!'
    
    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)