# Epic Title: Display reviews on product detail pages

import logging
from flask import Blueprint, jsonify, request
from backend.reviews.repositories.review_repository import ReviewRepository

review_bp = Blueprint('review', __name__)
review_repository = ReviewRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@review_bp.route('/product/<int:product_id>/reviews', methods=['GET'])
def get_reviews(product_id: int):
    reviews = review_repository.get_reviews_by_product_id(product_id)
    review_dicts = [review.__dict__ for review in reviews]
    
    rating_summary = review_repository.get_rating_summary_by_product_id(product_id)
    
    return jsonify({
        'reviews': review_dicts,
        'rating_summary': rating_summary
    }), 200