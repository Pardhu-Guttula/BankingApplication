# Epic Title: Track sales performance metrics

import logging
from flask import Blueprint, jsonify, request
import datetime
from backend.analytics.repositories.sales_repository import SalesRepository

sales_bp = Blueprint('sales', __name__)
sales_repository = SalesRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@sales_bp.route('/sales/daily', methods=['GET'])
def get_daily_sales():
    date_str = request.args.get('date')
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    daily_sales = sales_repository.get_daily_sales(date)
    sales_dicts = [sale.__dict__ for sale in daily_sales]
    return jsonify(sales_dicts), 200

@sales_bp.route('/sales/weekly', methods=['GET'])
def get_weekly_sales():
    date_str = request.args.get('date')
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    weekly_sales = sales_repository.get_weekly_sales(date)
    sales_dicts = [sale.__dict__ for sale in weekly_sales]
    return jsonify(sales_dicts), 200

@sales_bp.route('/sales/monthly', methods=['GET'])
def get_monthly_sales():
    date_str = request.args.get('date')
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    monthly_sales = sales_repository.get_monthly_sales(date)
    sales_dicts = [sale.__dict__ for sale in monthly_sales]
    return jsonify(sales_dicts), 200