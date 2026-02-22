# Epic Title: Implement review submission form

import logging
from flask import Flask
from flask_login import LoginManager
from backend.reviews.routes import app as reviews_app

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(reviews_app)
    
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        # The actual loading of user should be implemented 
        pass
    
    @app.route('/')
    def home():
        return 'Welcome to the Product Review System!'
    
    return app

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    app.run(debug=True)