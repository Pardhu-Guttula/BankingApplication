# Epic Title: Display reviews on product detail pages

from backend.reviews.models.review import Review
import mysql.connector

class ReviewRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_reviews_by_product_id(self, product_id: int) -> list[Review]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT review_id, product_id, user_id, rating, title, review_text, moderated, created_at
                FROM reviews 
                WHERE product_id = %s AND moderated = 1
                ORDER BY created_at DESC
            """, (product_id,))
            rows = cursor.fetchall()
            reviews = [Review(
                        review_id=row[0], 
                        product_id=row[1], 
                        user_id=row[2], 
                        rating=row[3], 
                        title=row[4], 
                        review_text=row[5], 
                        moderated=row[6], 
                        created_at=row[7]
                    ) for row in rows]
            return reviews
        finally:
            cursor.close()
            connection.close()

    def get_rating_summary_by_product_id(self, product_id: int) -> float:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT AVG(rating) as average_rating
                FROM reviews 
                WHERE product_id = %s AND moderated = 1
            """, (product_id,))
            result = cursor.fetchone()
            return result[0] if result else 0.0
        finally:
            cursor.close()
            connection.close()