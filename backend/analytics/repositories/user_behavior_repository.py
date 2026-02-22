# Epic Title: Monitor user behavior metrics

from backend.analytics.models.user_session import UserSession, PageView, ClickThroughRate
import mysql.connector

class UserBehaviorRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_average_session_duration(self) -> float:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT AVG(TIMESTAMPDIFF(SECOND, start_time, end_time)) as average_duration
                FROM user_sessions
            """)
            result = cursor.fetchone()
            return result[0] if result else 0.0
        finally:
            cursor.close()
            connection.close()

    def get_total_page_views(self) -> int:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT COUNT(*) as total_views
                FROM page_views
            """)
            result = cursor.fetchone()
            return result[0] if result else 0
        finally:
            cursor.close()
            connection.close()

    def get_click_through_rates(self) -> list:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT element_id, COUNT(*) as total_clicks
                FROM click_through_rates
                WHERE clicked = 1
                GROUP BY element_id
            """)
            rows = cursor.fetchall()
            click_rates = [{'element_id': row[0], 'total_clicks': row[1]} for row in rows]
            return click_rates
        finally:
            cursor.close()
            connection.close()