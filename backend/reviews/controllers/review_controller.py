# Epic Title: Implement review submission form

import logging
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
import datetime
from backend.reviews.models.review import Review
from backend.reviews.repositories.review_repository import ReviewRepository

review_bp = Blueprint('review', __name__)
review_repository = ReviewRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@review_bp.route('/review/submit', methods=['POST'])
@login_required
def submit_review():
    data = request.get_json()
    
    if not data or not all(field in data for field in ['product_id', 'rating', 'title', 'review_text']):
        return jsonify({'error': 'Incomplete fields'}), 400
    
    rating = data.get('rating')
    if rating < 1 or rating > 5:
        return jsonify({'error': 'Invalid rating'}), 400
    
    review = Review(
        review_id=None,
        product_id=data.get('product_id'),
        user_id=current_user.id,
        rating=rating,
        title=data.get('title'),
        review_text=data.get('review_text'),
        created_at=datetime.datetime.now()
    )
    
    success = review_repository.save_review(review)
    
    if success:
        return jsonify({'message': 'Review submitted successfully'}), 200
    else:
        return jsonify({'error': 'Failed to submit review'}), 500