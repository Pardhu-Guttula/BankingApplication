# Epic Title: Display reviews on product detail pages

from flask import Flask
from backend.reviews.controllers.review_controller import review_bp

app = Flask(__name__)
app.register_blueprint(review_bp)