# Epic Title: Review Submission

from sqlalchemy.orm import Session
from backend.product_reviews.models.review import Review

class ReviewRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_review(self, user_id: int, product_id: int, rating: float, title: str, review_text: str) -> Review:
        review = Review(
            user_id=user_id,
            product_id=product_id,
            rating=rating,
            title=title,
            review_text=review_text
        )
        self.db.add(review)
        self.db.commit()
        self.db.refresh(review)
        return review

    def get_reviews_by_product_id(self, product_id: int) -> list:
        return self.db.query(Review).filter(Review.product_id==product_id).all()