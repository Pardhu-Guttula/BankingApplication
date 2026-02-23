# Epic Title: Generate Detailed E-commerce Performance Reports

from sqlalchemy.orm import Session
from backend.analytics_reporting.models.performance import Performance

class PerformanceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_daily_performance(self, date: str) -> list:
        return self.db.query(Performance).filter(Performance.date == date).all()

    def get_weekly_performance(self, start_date: str, end_date: str) -> list:
        return self.db.query(Performance).filter(Performance.date >= start_date, Performance.date <= end_date).all()

    def get_monthly_performance(self, year: int, month: int) -> list:
        return self.db.query(Performance).filter(Performance.date.year == year, Performance.date.month == month).all()

    def create_performance(self, date: str, metric_name: str, metric_value: float) -> Performance:
        performance = Performance(
            date=date,
            metric_name=metric_name,
            metric_value=metric_value
        )
        self.db.add(performance)
        self.db.commit()
        self.db.refresh(performance)
        return performance