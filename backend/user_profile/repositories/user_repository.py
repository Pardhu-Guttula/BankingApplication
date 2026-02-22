# Epic Title: Change Password

from backend.user_profile.models.user_profile import UserProfile
import mysql.connector

class UserRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_user_by_id(self, user_id: int) -> UserProfile:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT user_id, email, hashed_password FROM users WHERE user_id = %s", (user_id,))
            user_result = cursor.fetchone()
            
            if user_result:
                return UserProfile(user_id=user_result[0], email=user_result[1], hashed_password=user_result[2])
            else:
                return None
        finally:
            cursor.close()
            connection.close()

    def update_password(self, user_id: int, new_hashed_password: str) -> bool:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                UPDATE users
                SET hashed_password = %s
                WHERE user_id = %s
            """, (new_hashed_password, user_id))
            
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            logging.error(f'Failed to update password: {e}')
            return False
        finally:
            cursor.close()
            connection.close()