# Epic Title: Review Submission

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.product_reviews.repositories.review_repository import ReviewRepository
from backend.product_reviews.services.review_service import ReviewService

review_bp = Blueprint('review', __name__)

@review_bp.route('/reviews/create', methods=['POST'])
def create_review():
    db = next(get_db())
    data = request.get_json()

    user_id = data.get('user_id')
    product_id = data.get('product_id')
    rating = data.get('rating')
    title = data.get('title')
    review_text = data.get('review_text')

    review_repository = ReviewRepository(db)
    review_service = ReviewService(review_repository)

    try:
        result = review_service.create_review(db, user_id, product_id, rating, title, review_text)
        if result['success']:
            review = result['review']
            return jsonify({
                "id": review.id,
                "user_id": review.user_id,
                "product_id": review.product_id,
                "rating": review.rating,
                "title": review.title,
                "review_text": review.review_text,
                "created_at": review.created_at
            }), 201
        return jsonify({"error": result.get("error")}), 400
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@review_bp.route('/reviews/product/<product_id>', methods=['GET'])
def get_reviews_by_product_id(product_id: int):
    db = next(get_db())

    review_repository = ReviewRepository(db)
    review_service = ReviewService(review_repository)

    try:
        reviews = review_service.get_reviews_by_product_id(db, product_id)
        reviews_data = [{
            "id": review.id,
            "user_id": review.user_id,
            "product_id": review.product_id,
            "rating": review.rating,
            "title": review.title,
            "review_text": review.review_text,
            "created_at": review.created_at
        } for review in reviews]
        return jsonify(reviews_data), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500