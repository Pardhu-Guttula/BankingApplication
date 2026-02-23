# Epic Title: Develop User Logout Capability

from flask import Flask
from backend.authentication.controllers.login_controller import login_bp
from backend.authentication.controllers.logout_controller import logout_bp
from backend.database.config import Base, engine

app = Flask(__name__)

# Register blueprints
app.register_blueprint(login_bp, url_prefix='/api/auth')
app.register_blueprint(logout_bp, url_prefix='/api/auth')

@app.before_first_request
def startup():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown(exception):
    # Code to run on shutdown, e.g., close db connection, clean up resources
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)