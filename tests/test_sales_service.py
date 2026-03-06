# File: tests/test_sales_service.py

import unittest
from unittest.mock import Mock
from sqlalchemy.orm import Session
from backend.analytics.services.sales_service import SalesService
from backend.analytics.repositories.sales_repository import SalesRepository

class TestSalesService(unittest.TestCase):

    def setUp(self):
        self.mock_sales_repository = Mock(spec=SalesRepository)
        self.sales_service = SalesService(self.mock_sales_repository)
        self.mock_db = Mock(spec=Session)

    def test_get_daily_sales_success(self):
        # Arrange
        date = "2023-10-12"
        sales_data = [Mock(amount=100), Mock(amount=200)]
        self.mock_sales_repository.get_daily_sales.return_value = sales_data
        
        # Act
        result = self.sales_service.get_daily_sales(self.mock_db, date)

        # Assert
        self.mock_sales_repository.get_daily_sales.assert_called_once_with(date)
        self.assertEqual(result, {"date": date, "total_amount": 300, "sales": sales_data})

    def test_get_daily_sales_empty(self):
        # Arrange
        date = "2023-10-12"
        self.mock_sales_repository.get_daily_sales.return_value = []
        
        # Act
        result = self.sales_service.get_daily_sales(self.mock_db, date)

        # Assert
        self.mock_sales_repository.get_daily_sales.assert_called_once_with(date)
        self.assertEqual(result, {"date": date, "total_amount": 0, "sales": []})

    def test_get_daily_sales_invalid_date(self):
        # Arrange
        date = "invalid-date"
        self.mock_sales_repository.get_daily_sales.side_effect = ValueError("Invalid date format")

        # Act & Assert
        with self.assertRaises(ValueError):
            self.sales_service.get_daily_sales(self.mock_db, date)

    def test_get_weekly_sales_success(self):
        # Arrange
        start_date = "2023-10-01"
        end_date = "2023-10-07"
        sales_data = [Mock(amount=100), Mock(amount=200), Mock(amount=300)]
        self.mock_sales_repository.get_weekly_sales.return_value = sales_data
        
        # Act
        result = self.sales_service.get_weekly_sales(self.mock_db, start_date, end_date)

        # Assert
        self.mock_sales_repository.get_weekly_sales.assert_called_once_with(start_date, end_date)
        self.assertEqual(result, {"start_date": start_date, "end_date": end_date, "total_amount": 600, "sales": sales_data})

    def test_get_weekly_sales_no_sales(self):
        # Arrange
        start_date = "2023-10-01"
        end_date = "2023-10-07"
        self.mock_sales_repository.get_weekly_sales.return_value = []
        
        # Act
        result = self.sales_service.get_weekly_sales(self.mock_db, start_date, end_date)

        # Assert
        self.mock_sales_repository.get_weekly_sales.assert_called_once_with(start_date, end_date)
        self.assertEqual(result, {"start_date": start_date, "end_date": end_date, "total_amount": 0, "sales": []})

    def test_get_weekly_sales_invalid_date_range(self):
        # Arrange
        start_date = "2023-10-07"
        end_date = "2023-10-01"
        self.mock_sales_repository.get_weekly_sales.side_effect = ValueError("Invalid date range")

        # Act & Assert
        with self.assertRaises(ValueError):
            self.sales_service.get_weekly_sales(self.mock_db, start_date, end_date)

    def test_get_monthly_sales_success(self):
        # Arrange
        year = 2023
        month = 10
        sales_data = [Mock(amount=100), Mock(amount=200), Mock(amount=300), Mock(amount=400)]
        self.mock_sales_repository.get_monthly_sales.return_value = sales_data
        
        # Act
        result = self.sales_service.get_monthly_sales(self.mock_db, year, month)

        # Assert
        self.mock_sales_repository.get_monthly_sales.assert_called_once_with(year, month)
        self.assertEqual(result, {"year": year, "month": month, "total_amount": 1000, "sales": sales_data})

    def test_get_monthly_sales_no_sales(self):
        # Arrange
        year = 2023
        month = 10
        self.mock_sales_repository.get_monthly_sales.return_value = []
        
        # Act
        result = self.sales_service.get_monthly_sales(self.mock_db, year, month)

        # Assert
        self.mock_sales_repository.get_monthly_sales.assert_called_once_with(year, month)
        self.assertEqual(result, {"year": year, "month": month, "total_amount": 0, "sales": []})

    def test_get_monthly_sales_invalid_date(self):
        # Arrange
        year = "invalid"
        month = "invalid"
        self.mock_sales_repository.get_monthly_sales.side_effect = ValueError("Invalid year or month")

        # Act & Assert
        with self.assertRaises(ValueError):
            self.sales_service.get_monthly_sales(self.mock_db, year, month)

if __name__ == '__main__':
    unittest.main()
