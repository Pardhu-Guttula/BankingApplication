# Epic Title: Implement review submission form

from backend.reviews.models.review import Review
import mysql.connector

class ReviewRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def save_review(self, review: Review) -> bool:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO reviews (product_id, user_id, rating, title, review_text, created_at)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (review.product_id, review.user_id, review.rating, review.title, review.review_text, review.created_at))
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            logging.error(f'Failed to save review: {e}')
            return False
        finally:
            cursor.close()
            connection.close()