# Epic Title: Track Sales Performance Metrics

from sqlalchemy.orm import Session
from backend.analytics.models.sales import Sales

class SalesRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_daily_sales(self, date: str) -> list:
        return self.db.query(Sales).filter(Sales.date == date).all()

    def get_weekly_sales(self, start_date: str, end_date: str) -> list:
        return self.db.query(Sales).filter(Sales.date >= start_date, Sales.date <= end_date).all()

    def get_monthly_sales(self, year: int, month: int) -> list:
        return self.db.query(Sales).filter(Sales.date.year == year, Sales.date.month == month).all()