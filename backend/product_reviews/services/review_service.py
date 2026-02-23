# Epic Title: Review Display

from sqlalchemy.orm import Session
from backend.product_reviews.repositories.review_repository import ReviewRepository

class ReviewService:
    def __init__(self, review_repository: ReviewRepository):
        self.review_repository = review_repository

    def get_approved_reviews_by_product_id(self, db: Session, product_id: int):
        reviews = self.review_repository.get_approved_reviews_by_product_id(product_id)
        return reviews

    def get_average_rating_for_product(self, db: Session, product_id: int) -> float:
        return self.review_repository.get_average_rating_for_product(product_id)

    def create_review(self, db: Session, user_id: int, product_id: int, rating: float, title: str, review_text: str) -> dict:
        review = self.review_repository.create_review(user_id, product_id, rating, title, review_text)
        return {"success": True, "review": review}

    def approve_review(self, db: Session, review_id: int) -> dict:
        review = self.review_repository.approve_review(review_id)
        return {"success": True, "review": review}