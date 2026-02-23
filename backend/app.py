# Epic Title: Implement Overall Design Framework for the E-commerce Platform

from flask import Flask
from backend.design.controllers.layout_controller import layout_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(layout_bp)

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