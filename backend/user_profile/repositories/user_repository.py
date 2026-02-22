# Epic Title: Update Personal Information

from backend.user_profile.models.user_profile import UserProfile
import datetime
import mysql.connector

class UserRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def update_user_profile(self, user_profile: UserProfile) -> bool:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                UPDATE users 
                SET name = %s, email = %s, address = %s, updated_at = %s 
                WHERE user_id = %s
            """, (user_profile.name, user_profile.email, user_profile.address, user_profile.updated_at, user_profile.user_id))
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            logging.error(f'Failed to update user profile: {e}')
            return False
        finally:
            cursor.close()
            connection.close()