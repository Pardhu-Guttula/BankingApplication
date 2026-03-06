import pytest
import json
from flask import Flask
from backend.analytics.controllers.sales_controller import sales_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(sales_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test for getting daily sales

def test_get_daily_sales_success(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_daily_sales', return_value={
        "date": "2023-10-10",
        "total_amount": 1000.0,
        "sales": []
    })
    response = client.get('/sales/daily?date=2023-10-10')
    assert response.status_code == 200
    assert response.json == {
        "date": "2023-10-10",
        "total_amount": 1000.0,
        "sales": []
    }

def test_get_daily_sales_failure(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_daily_sales', side_effect=Exception("Unable to process your request"))
    response = client.get('/sales/daily?date=2023-10-10')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}

# Test for getting weekly sales

def test_get_weekly_sales_success(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_weekly_sales', return_value={
        "start_date": "2023-10-01",
        "end_date": "2023-10-07",
        "total_amount": 7000.0,
        "sales": []
    })
    response = client.get('/sales/weekly?start_date=2023-10-01&end_date=2023-10-07')
    assert response.status_code == 200
    assert response.json == {
        "start_date": "2023-10-01",
        "end_date": "2023-10-07",
        "total_amount": 7000.0,
        "sales": []
    }

def test_get_weekly_sales_failure(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_weekly_sales', side_effect=Exception("Unable to process your request"))
    response = client.get('/sales/weekly?start_date=2023-10-01&end_date=2023-10-07')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}

# Test for getting monthly sales

def test_get_monthly_sales_success(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_monthly_sales', return_value={
        "year": 2023,
        "month": 10,
        "total_amount": 30000.0,
        "sales": []
    })
    response = client.get('/sales/monthly?year=2023&month=10')
    assert response.status_code == 200
    assert response.json == {
        "year": 2023,
        "month": 10,
        "total_amount": 30000.0,
        "sales": []
    }

def test_get_monthly_sales_failure(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_monthly_sales', side_effect=Exception("Unable to process your request"))
    response = client.get('/sales/monthly?year=2023&month=10')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}
