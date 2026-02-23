# Epic Title: Review Display

from sqlalchemy.orm import Session
from backend.product_reviews.models.review import Review

class ReviewRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_approved_reviews_by_product_id(self, product_id: int) -> list:
        return self.db.query(Review).filter(Review.product_id == product_id, Review.approved == True).order_by(Review.created_at.desc()).all()

    def get_average_rating_for_product(self, product_id: int) -> float:
        reviews = self.db.query(Review).filter(Review.product_id == product_id, Review.approved == True).all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0.0

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

    def approve_review(self, review_id: int) -> Review:
        review = self.db.query(Review).filter(Review.id == review_id).first()
        if review:
            review.approved = True
            self.db.commit()
            self.db.refresh(review)
        return review