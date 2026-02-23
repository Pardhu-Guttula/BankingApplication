# Epic Title: Generate Detailed E-commerce Performance Reports

from sqlalchemy.orm import Session
from backend.analytics_reporting.repositories.performance_repository import PerformanceRepository

class PerformanceService:
    def __init__(self, performance_repository: PerformanceRepository):
        self.performance_repository = performance_repository

    def get_daily_performance(self, db: Session, date: str):
        performances = self.performance_repository.get_daily_performance(date)
        return {"date": date, "performances": performances}

    def get_weekly_performance(self, db: Session, start_date: str, end_date: str):
        performances = self.performance_repository.get_weekly_performance(start_date, end_date)
        return {"start_date": start_date, "end_date": end_date, "performances": performances}

    def get_monthly_performance(self, db: Session, year: int, month: int):
        performances = self.performance_repository.get_monthly_performance(year, month)
        return {"year": year, "month": month, "performances": performances}

    def create_performance(self, db: Session, date: str, metric_name: str, metric_value: float) -> dict:
        performance = self.performance_repository.create_performance(date, metric_name, metric_value)
        return {"success": True, "performance": performance}