# File: tests/test_sales_performance.py
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.analytics.v1.track_sales_performance import sales_bp
from sqlalchemy.exc import SQLAlchemyError

@pytest.fixture

def app():
    app = Flask(__name__)
    app.register_blueprint(sales_bp)
    return app

@pytest.fixture

def client(app):
    return app.test_client()

# Mocked get_db generator
def mock_get_db():
    yield MagicMock()

# Positive test case for daily sales
@patch('backend.analytics.v1.track_sales_performance.get_db', mock_get_db)
@patch('backend.analytics.repositories.sales_repository.SalesRepository')
@patch('backend.analytics.services.sales_service.SalesService')
def test_get_daily_sales_success(mock_sales_service, mock_sales_repository, client):
    mock_sales_service.return_value.get_daily_sales.return_value = [{'date': '2023-10-01', 'total_sales': 1500}]
    response = client.get('/sales/daily?date=2023-10-01')
    assert response.status_code == 200
    assert response.json == [{'date': '2023-10-01', 'total_sales': 1500}]

# Negative test case for daily sales 
@patch('backend.analytics.v1.track_sales_performance.get_db', mock_get_db)
@patch('backend.analytics.repositories.sales_repository.SalesRepository')
@patch('backend.analytics.services.sales_service.SalesService')
def test_get_daily_sales_failure(mock_sales_service, mock_sales_repository, client):
    mock_sales_service.return_value.get_daily_sales.side_effect = SQLAlchemyError
    response = client.get('/sales/daily?date=2023-10-01')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}

# Edge case for daily sales with no date
def test_get_daily_sales_no_date(client):
    response = client.get('/sales/daily')
    assert response.status_code == 400
# Positive test case for weekly sales
@patch('backend.analytics.v1.track_sales_performance.get_db', mock_get_db)
@patch('backend.analytics.repositories.sales_repository.SalesRepository')
@patch('backend.analytics.services.sales_service.SalesService')
def test_get_weekly_sales_success(mock_sales_service, mock_sales_repository, client):
    mock_sales_service.return_value.get_weekly_sales.return_value = [{'week': '2023-10-01', 'total_sales': 10500}]
    response = client.get('/sales/weekly?start_date=2023-10-01&end_date=2023-10-07')
    assert response.status_code == 200
    assert response.json == [{'week': '2023-10-01', 'total_sales': 10500}]

# Negative test case for weekly sales 
@patch('backend.analytics.v1.track_sales_performance.get_db', mock_get_db)
@patch('backend.analytics.repositories.sales_repository.SalesRepository')
@patch('backend.analytics.services.sales_service.SalesService')
def test_get_weekly_sales_failure(mock_sales_service, mock_sales_repository, client):
    mock_sales_service.return_value.get_weekly_sales.side_effect = SQLAlchemyError
    response = client.get('/sales/weekly?start_date=2023-10-01&end_date=2023-10-07')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}

# Edge case for weekly sales with no dates
def test_get_weekly_sales_no_dates(client):
    response = client.get('/sales/weekly')
    assert response.status_code == 400
# Positive test case for monthly sales
@patch('backend.analytics.v1.track_sales_performance.get_db', mock_get_db)
@patch('backend.analytics.repositories.sales_repository.SalesRepository')
@patch('backend.analytics.services.sales_service.SalesService')
def test_get_monthly_sales_success(mock_sales_service, mock_sales_repository, client):
    mock_sales_service.return_value.get_monthly_sales.return_value = [{'month': '2023-10', 'total_sales': 45000}]
    response = client.get('/sales/monthly?year=2023&month=10')
    assert response.status_code == 200
    assert response.json == [{'month': '2023-10', 'total_sales': 45000}]

# Negative test case for monthly sales 
@patch('backend.analytics.v1.track_sales_performance.get_db', mock_get_db)
@patch('backend.analytics.repositories.sales_repository.SalesRepository')
@patch('backend.analytics.services.sales_service.SalesService')
def test_get_monthly_sales_failure(mock_sales_service, mock_sales_repository, client):
    mock_sales_service.return_value.get_monthly_sales.side_effect = SQLAlchemyError
    response = client.get('/sales/monthly?year=2023&month=10')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}

# Edge case for monthly sales with invalid month
def test_get_monthly_sales_invalid_month(client):
    response = client.get('/sales/monthly?year=2023&month=13')
    assert response.status_code == 400
# Edge case for monthly sales with invalid year
def test_get_monthly_sales_invalid_year(client):
    response = client.get('/sales/monthly?year=abcd&month=10')
    assert response.status_code == 400
