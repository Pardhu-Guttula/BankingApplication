# Epic Title: Store Order Information in PostgreSQL Database

from flask import Flask
from backend.orders.controllers.order_controller import order_bp
from backend.database.config import Base, engine

app = Flask(__name__)

# Register blueprints
app.register_blueprint(order_bp, url_prefix='/api')

@app.before_first_request
def startup():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown(exception):
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)