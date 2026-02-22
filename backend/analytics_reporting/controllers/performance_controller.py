# Epic Title: Generate detailed e-commerce performance reports

import logging
from flask import Blueprint, jsonify, request
import datetime
from backend.analytics_reporting.repositories.performance_repository import PerformanceRepository

performance_bp = Blueprint('performance', __name__)
performance_repository = PerformanceRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@performance_bp.route('/report/daily', methods=['GET'])
def get_daily_report():
    date_str = request.args.get('date')
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    daily_performance = performance_repository.get_daily_performance(date)
    return jsonify(daily_performance.__dict__), 200

@performance_bp.route('/report/weekly', methods=['GET'])
def get_weekly_report():
    date_str = request.args.get('date')
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    weekly_performance = performance_repository.get_weekly_performance(date)
    performance_dicts = [performance.__dict__ for performance in weekly_performance]
    return jsonify(performance_dicts), 200

@performance_bp.route('/report/monthly', methods=['GET'])
def get_monthly_report():
    date_str = request.args.get('date')
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    monthly_performance = performance_repository.get_monthly_performance(date)
    performance_dicts = [performance.__dict__ for performance in monthly_performance]
    return jsonify(performance_dicts), 200