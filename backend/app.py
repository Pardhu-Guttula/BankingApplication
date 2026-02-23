# Epic Title: Design and Implement Header for the E-commerce Platform

from flask import Flask
from backend.personalized_dashboard.controllers.header_controller import header_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(header_bp, url_prefix='/ui')

@app.before_first_request
def startup():
    # Code to run on startup, e.g., initializing loggers, checking preconditions
    pass

@app.teardown_appcontext
def shutdown(exception):
    # Code to run on shutdown, e.g., close db connection, clean up resources
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)