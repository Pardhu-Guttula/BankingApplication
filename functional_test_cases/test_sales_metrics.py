import pytest
from flask import Flask
from backend.analytics.controllers.sales_controller import sales_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(sales_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()


def test_get_daily_sales_success(client, mocker):
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_daily_sales', return_value={
        "date": "2023-10-01",
        "total_amount": 15000.0,
        "sales": []
    })

    response = client.get('/sales/daily?date=2023-10-01')
    assert response.status_code == 200
    assert response.json == {
        "date": "2023-10-01",
        "total_amount": 15000.0,
        "sales": []
    }


def test_get_daily_sales_error(client, mocker):
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_daily_sales', side_effect=Exception('DB Error'))

    response = client.get('/sales/daily?date=2023-10-01')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}


def test_get_weekly_sales_success(client, mocker):
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_weekly_sales', return_value={
        "start_date": "2023-10-01",
        "end_date": "2023-10-07",
        "total_amount": 90000.0,
        "sales": []
    })

    response = client.get('/sales/weekly?start_date=2023-10-01&end_date=2023-10-07')
    assert response.status_code == 200
    assert response.json == {
        "start_date": "2023-10-01",
        "end_date": "2023-10-07",
        "total_amount": 90000.0,
        "sales": []
    }


def test_get_weekly_sales_error(client, mocker):
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_weekly_sales', side_effect=Exception('DB Error'))

    response = client.get('/sales/weekly?start_date=2023-10-01&end_date=2023-10-07')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}


def test_get_monthly_sales_success(client, mocker):
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_monthly_sales', return_value={
        "year": 2023,
        "month": 10,
        "total_amount": 380000.0,
        "sales": []
    })

    response = client.get('/sales/monthly?year=2023&month=10')
    assert response.status_code == 200
    assert response.json == {
        "year": 2023,
        "month": 10,
        "total_amount": 380000.0,
        "sales": []
    }


def test_get_monthly_sales_error(client, mocker):
    mocker.patch('backend.analytics.services.sales_service.SalesService.get_monthly_sales', side_effect=Exception('DB Error'))

    response = client.get('/sales/monthly?year=2023&month=10')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}
