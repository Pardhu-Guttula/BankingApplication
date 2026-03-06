# File: tests/test_sales_repository.py

import unittest
from unittest.mock import MagicMock
from backend.analytics.models.sales import Sales
from sqlalchemy.orm import Session
from datetime import date
from sales_repository import SalesRepository

class TestSalesRepository(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock(spec=Session)
        self.repository = SalesRepository(self.mock_db)

    def test_get_daily_sales(self):
        date_str = "2023-10-05"
        expected_sales = [Sales(id=1, date=date(2023, 10, 5), amount=100.0)]
        self.mock_db.query().filter().all.return_value = expected_sales

        result = self.repository.get_daily_sales(date_str)
        self.assertEqual(result, expected_sales)

    def test_get_daily_sales_no_results(self):
        date_str = "2023-10-05"
        self.mock_db.query().filter().all.return_value = []

        result = self.repository.get_daily_sales(date_str)
        self.assertEqual(result, [])

    def test_get_weekly_sales(self):
        start_date = "2023-10-01"
        end_date = "2023-10-07"
        expected_sales = [Sales(id=1, date=date(2023, 10, 5), amount=100.0), Sales(id=2, date=date(2023, 10, 6), amount=150.0)]
        self.mock_db.query().filter().all.return_value = expected_sales

        result = self.repository.get_weekly_sales(start_date, end_date)
        self.assertEqual(result, expected_sales)

    def test_get_weekly_sales_no_results(self):
        start_date = "2023-10-01"
        end_date = "2023-10-07"
        self.mock_db.query().filter().all.return_value = []

        result = self.repository.get_weekly_sales(start_date, end_date)
        self.assertEqual(result, [])

    def test_get_monthly_sales(self):
        year = 2023
        month = 10
        expected_sales = [Sales(id=1, date=date(2023, 10, 5), amount=100.0), Sales(id=2, date=date(2023, 10, 20), amount=150.0)]
        self.mock_db.query().filter().all.return_value = expected_sales

        result = self.repository.get_monthly_sales(year, month)
        self.assertEqual(result, expected_sales)

    def test_get_monthly_sales_no_results(self):
        year = 2023
        month = 10
        self.mock_db.query().filter().all.return_value = []

        result = self.repository.get_monthly_sales(year, month)
        self.assertEqual(result, [])
