# Epic Title: Track Sales Performance Metrics

from sqlalchemy.orm import Session
from backend.analytics.repositories.sales_repository import SalesRepository

class SalesService:
    def __init__(self, sales_repository: SalesRepository):
        self.sales_repository = sales_repository

    def get_daily_sales(self, db: Session, date: str):
        sales = self.sales_repository.get_daily_sales(date)
        total_amount = sum(sale.amount for sale in sales)
        return {"date": date, "total_amount": total_amount, "sales": sales}

    def get_weekly_sales(self, db: Session, start_date: str, end_date: str):
        sales = self.sales_repository.get_weekly_sales(start_date, end_date)
        total_amount = sum(sale.amount for sale in sales)
        return {"start_date": start_date, "end_date": end_date, "total_amount": total_amount, "sales": sales}

    def get_monthly_sales(self, db: Session, year: int, month: int):
        sales = self.sales_repository.get_monthly_sales(year, month)
        total_amount = sum(sale.amount for sale in sales)
        return {"year": year, "month": month, "total_amount": total_amount, "sales": sales}