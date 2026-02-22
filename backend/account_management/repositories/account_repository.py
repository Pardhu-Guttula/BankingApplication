# Epic Title: Manage Account

from backend.account_management.models.account_settings import AccountSettings
import mysql.connector

class AccountRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_account_settings_by_user_id(self, user_id: int) -> AccountSettings:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT user_id, preferences, privacy_settings, updated_at FROM account_settings WHERE user_id = %s", (user_id,))
            settings_result = cursor.fetchone()
            
            if settings_result:
                return AccountSettings(
                    user_id=settings_result[0], 
                    preferences=settings_result[1], 
                    privacy_settings=settings_result[2], 
                    updated_at=settings_result[3]
                )
            else:
                return None
        finally:
            cursor.close()
            connection.close()

    def update_account_settings(self, account_settings: AccountSettings) -> bool:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                UPDATE account_settings 
                SET preferences = %s, privacy_settings = %s, updated_at = %s 
                WHERE user_id = %s
            """, (account_settings.preferences, account_settings.privacy_settings, account_settings.updated_at, account_settings.user_id))
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            logging.error(f'Failed to update account settings: {e}')
            return False
        finally:
            cursor.close()
            connection.close()