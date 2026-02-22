# Epic Title: Track sales performance metrics

import logging
from flask import Flask
from backend.analytics.routes import app as analytics_app

def create_app():
    app = Flask(__name__)
    app.register_blueprint(analytics_app)
    
    @app.route('/')
    def home():
        return 'Welcome to the Sales Analytics System!'
    
    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)