# Epic Title: Review Submission

from sqlalchemy.orm import Session
from backend.product_reviews.repositories.review_repository import ReviewRepository

class ReviewService:
    RATING_RANGE_ERROR = "Rating must be between 1 and 5."

    def __init__(self, review_repository: ReviewRepository):
        self.review_repository = review_repository

    def validate_rating(self, rating: float) -> bool:
        return 1 <= rating <= 5

    def create_review(self, db: Session, user_id: int, product_id: int, rating: float, title: str, review_text: str) -> dict:
        if not self.validate_rating(rating):
            return {"success": False, "error": self.RATING_RANGE_ERROR}
        review = self.review_repository.create_review(user_id, product_id, rating, title, review_text)
        return {"success": True, "review": review}

    def get_reviews_by_product_id(self, db: Session, product_id: int):
        reviews = self.review_repository.get_reviews_by_product_id(product_id)
        return reviews