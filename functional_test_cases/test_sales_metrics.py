import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.analytics.controllers.sales_controller import sales_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(sales_bp)
    return app

@pytest.fixture
def client(app: Flask):
    return app.test_client()

# Test cases for get_daily_sales endpoint

def test_get_daily_sales_success(client: FlaskClient):
    response = client.get('/sales/daily?date=2023-01-01')
    assert response.status_code == 200  # status code inferred - not explicit in source


def test_get_daily_sales_not_found(client: FlaskClient):
    response = client.get('/sales/daily?date=9999-01-01')
    assert response.status_code == 200  # status code inferred - not explicit in source

# Test cases for get_weekly_sales endpoint

def test_get_weekly_sales_success(client: FlaskClient):
    response = client.get('/sales/weekly?start_date=2023-01-01&end_date=2023-01-07')
    assert response.status_code == 200  # status code inferred - not explicit in source


def test_get_weekly_sales_not_found(client: FlaskClient):
    response = client.get('/sales/weekly?start_date=9999-01-01&end_date=9999-01-07')
    assert response.status_code == 200  # status code inferred - not explicit in source

# Test cases for get_monthly_sales endpoint

def test_get_monthly_sales_success(client: FlaskClient):
    response = client.get('/sales/monthly?year=2023&month=1')
    assert response.status_code == 200  # status code inferred - not explicit in source


def test_get_monthly_sales_not_found(client: FlaskClient):
    response = client.get('/sales/monthly?year=9999&month=1')
    assert response.status_code == 200  # status code inferred - not explicit in source
