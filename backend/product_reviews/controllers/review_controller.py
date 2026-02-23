# Epic Title: Review Display

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.product_reviews.repositories.review_repository import ReviewRepository
from backend.product_reviews.services.review_service import ReviewService

review_bp = Blueprint('review', __name__)

@review_bp.route('/reviews/product/<product_id>', methods=['GET'])
def get_reviews_by_product_id(product_id: int):
    db = next(get_db())

    review_repository = ReviewRepository(db)
    review_service = ReviewService(review_repository)

    try:
        reviews = review_service.get_approved_reviews_by_product_id(db, product_id)
        average_rating = review_service.get_average_rating_for_product(db, product_id)
        reviews_data = [{
            "id": review.id,
            "user_id": review.user_id,
            "product_id": review.product_id,
            "rating": review.rating,
            "title": review.title,
            "review_text": review.review_text,
            "created_at": review.created_at
        } for review in reviews]
        return jsonify({
            "reviews": reviews_data,
            "average_rating": average_rating
        }), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@review_bp.route('/reviews/approve/<review_id>', methods=['POST'])
def approve_review(review_id: int):
    db = next(get_db())

    review_repository = ReviewRepository(db)
    review_service = ReviewService(review_repository)

    try:
        result = review_service.approve_review(db, review_id)
        if result['success']:
            review = result['review']
            return jsonify({
                "id": review.id,
                "user_id": review.user_id,
                "product_id": review.product_id,
                "rating": review.rating,
                "title": review.title,
                "review_text": review.review_text,
                "approved": review.approved,
                "created_at": review.created_at
            }), 200
        return jsonify({"error": "Approval failed"}), 400
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500