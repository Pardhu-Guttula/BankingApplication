# Epic Title: Review Submission

from flask import Flask
from backend.product_reviews.controllers.review_controller import review_bp
from backend.database.config import Base, engine

app = Flask(__name__)

# Register blueprints
app.register_blueprint(review_bp, url_prefix='/api')

@app.before_first_request
def startup():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown(exception):
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)