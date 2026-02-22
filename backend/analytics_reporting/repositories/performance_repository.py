# Epic Title: Generate detailed e-commerce performance reports

from backend.analytics_reporting.models.performance_metrics import PerformanceMetrics
import mysql.connector

class PerformanceRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_daily_performance(self, date: datetime.date) -> PerformanceMetrics:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT metric_id, date, sales_quantity, total_revenue, avg_session_duration, total_page_views, click_through_rate
                FROM performance_metrics 
                WHERE date = %s
            """, (date,))
            row = cursor.fetchone()
            return PerformanceMetrics(
                        metric_id=row[0], 
                        date=row[1], 
                        sales_quantity=row[2], 
                        total_revenue=row[3], 
                        avg_session_duration=row[4], 
                        total_page_views=row[5], 
                        click_through_rate=row[6]
                    ) if row else None
        finally:
            cursor.close()
            connection.close()

    def get_weekly_performance(self, date: datetime.date) -> list[PerformanceMetrics]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT metric_id, date, sales_quantity, total_revenue, avg_session_duration, total_page_views, click_through_rate
                FROM performance_metrics 
                WHERE YEARWEEK(date, 1) = YEARWEEK(%s, 1)
            """, (date,))
            rows = cursor.fetchall()
            weekly_performance = [PerformanceMetrics(
                                    metric_id=row[0], 
                                    date=row[1], 
                                    sales_quantity=row[2], 
                                    total_revenue=row[3], 
                                    avg_session_duration=row[4], 
                                    total_page_views=row[5], 
                                    click_through_rate=row[6]
                                ) for row in rows]
            return weekly_performance
        finally:
            cursor.close()
            connection.close()

    def get_monthly_performance(self, date: datetime.date) -> list[PerformanceMetrics]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT metric_id, date, sales_quantity, total_revenue, avg_session_duration, total_page_views, click_through_rate
                FROM performance_metrics 
                WHERE YEAR(date) = YEAR(%s) AND MONTH(date) = MONTH(%s)
            """, (date, date))
            rows = cursor.fetchall()
            monthly_performance = [PerformanceMetrics(
                                    metric_id=row[0], 
                                    date=row[1], 
                                    sales_quantity=row[2], 
                                    total_revenue=row[3], 
                                    avg_session_duration=row[4], 
                                    total_page_views=row[5], 
                                    click_through_rate=row[6]
                                ) for row in rows]
            return monthly_performance
        finally:
            cursor.close()
            connection.close()