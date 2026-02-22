# Epic Title: Track sales performance metrics

from backend.analytics.models.sales import Sales
import mysql.connector

class SalesRepository:
    def __init__(self, db_config: dict):
        self.db_config = db_config
    
    def get_daily_sales(self, date: datetime.date) -> list[Sales]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT sale_id, product_id, quantity, total_price, sale_date
                FROM sales 
                WHERE sale_date = %s
            """, (date,))
            rows = cursor.fetchall()
            daily_sales = [Sales(
                            sale_id=row[0], 
                            product_id=row[1], 
                            quantity=row[2], 
                            total_price=row[3], 
                            sale_date=row[4]
                        ) for row in rows]
            return daily_sales
        finally:
            cursor.close()
            connection.close()

    def get_weekly_sales(self, date: datetime.date) -> list[Sales]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT sale_id, product_id, quantity, total_price, sale_date
                FROM sales 
                WHERE YEARWEEK(sale_date, 1) = YEARWEEK(%s, 1)
            """, (date,))
            rows = cursor.fetchall()
            weekly_sales = [Sales(
                            sale_id=row[0], 
                            product_id=row[1], 
                            quantity=row[2], 
                            total_price=row[3], 
                            sale_date=row[4]
                        ) for row in rows]
            return weekly_sales
        finally:
            cursor.close()
            connection.close()

    def get_monthly_sales(self, date: datetime.date) -> list[Sales]:
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        
        try:
            cursor.execute("""
                SELECT sale_id, product_id, quantity, total_price, sale_date
                FROM sales 
                WHERE YEAR(sale_date) = YEAR(%s) AND MONTH(sale_date) = MONTH(%s)
            """, (date, date))
            rows = cursor.fetchall()
            monthly_sales = [Sales(
                            sale_id=row[0], 
                            product_id=row[1], 
                            quantity=row[2], 
                            total_price=row[3], 
                            sale_date=row[4]
                        ) for row in rows]
            return monthly_sales
        finally:
            cursor.close()
            connection.close()