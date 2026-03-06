import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.analytics.controllers.sales_controller import sales_bp
import json

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(sales_bp)
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

# Test cases for GET /sales/daily

def test_get_daily_sales_success(client: FlaskClient):
    response = client.get('/sales/daily?date=2023-03-06')
    assert response.status_code == 200
    assert 'date' in response.json
    assert 'total_amount' in response.json
    assert 'sales' in response.json

@pytest.mark.parametrize("date", ["invalid-date", "2021-02-30"])
def test_get_daily_sales_failure(client: FlaskClient, date):
    response = client.get(f'/sales/daily?date={date}')
    assert response.status_code == 500
    assert 'error' in response.json

# Test cases for GET /sales/weekly

def test_get_weekly_sales_success(client: FlaskClient):
    response = client.get('/sales/weekly?start_date=2023-03-01&end_date=2023-03-07')
    assert response.status_code == 200
    assert 'start_date' in response.json
    assert 'end_date' in response.json
    assert 'total_amount' in response.json
    assert 'sales' in response.json

@pytest.mark.parametrize("start_date,end_date", [
    ("invalid-date", "2023-03-07"),
    ("2023-03-01", "invalid-date"),
])
def test_get_weekly_sales_failure(client: FlaskClient, start_date, end_date):
    response = client.get(f'/sales/weekly?start_date={start_date}&end_date={end_date}')
    assert response.status_code == 500
    assert 'error' in response.json

# Test cases for GET /sales/monthly

def test_get_monthly_sales_success(client: FlaskClient):
    response = client.get('/sales/monthly?year=2023&month=3')
    assert response.status_code == 200
    assert 'year' in response.json
    assert 'month' in response.json
    assert 'total_amount' in response.json
    assert 'sales' in response.json

@pytest.mark.parametrize("year,month", [
    (2023, "invalid-month"),
    ("invalid-year", 3),
])
def test_get_monthly_sales_failure(client: FlaskClient, year, month):
    response = client.get(f'/sales/monthly?year={year}&month={month}')
    assert response.status_code == 500
    assert 'error' in response.json
