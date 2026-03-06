import pytest
import requests

BASE_URL = "http://localhost:5000/sales"

@pytest.fixture
    def date():
    return "2023-10-20"

@pytest.fixture
    def week_range():
    return ("2023-10-15", "2023-10-21")

@pytest.fixture
    def month_period():
    return (2023, 10)


def test_get_daily_sales_success(date):
    response = requests.get(f"{BASE_URL}/daily?date={date}")
        assert response.status_code == 200
        assert "date" in response.json()
        assert "total_amount" in response.json()


def test_get_daily_sales_failure_invalid_date():
    response = requests.get(f"{BASE_URL}/daily?date=2023-02-30")
    assert response.status_code == 500
    assert "error" in response.json()


def test_get_weekly_sales_success(week_range):
    start_date, end_date = week_range
    response = requests.get(f"{BASE_URL}/weekly?start_date={start_date}&end_date={end_date}")
    assert response.status_code == 200
    assert "start_date" in response.json()
    assert "end_date" in response.json()
    assert "total_amount" in response.json()


def test_get_weekly_sales_failure_missing_date_range():
    response = requests.get(f"{BASE_URL}/weekly?start_date=2023-10-15")
    assert response.status_code == 500
    assert "error" in response.json()


def test_get_monthly_sales_success(month_period):
    year, month = month_period
    response = requests.get(f"{BASE_URL}/monthly?year={year}&month={month}")
    assert response.status_code == 200
    assert "year" in response.json()
    assert "month" in response.json()
    assert "total_amount" in response.json()


def test_get_monthly_sales_failure_invalid_period():
    response = requests.get(f"{BASE_URL}/monthly?year=2023&month=13")
    assert response.status_code == 500
    assert "error" in response.json()