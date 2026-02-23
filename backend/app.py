# Epic Title: Remove Products from the Shopping Cart

from flask import Flask
from backend.shopping_cart.controllers.cart_controller import cart_bp
from backend.database.config import Base, engine

app = Flask(__name__)

# Register blueprints
app.register_blueprint(cart_bp, url_prefix='/api')

@app.before_first_request
def startup():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown(exception):
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)