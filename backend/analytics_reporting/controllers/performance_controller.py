# Epic Title: Generate Detailed E-commerce Performance Reports

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.analytics_reporting.repositories.performance_repository import PerformanceRepository
from backend.analytics_reporting.services.performance_service import PerformanceService

performance_bp = Blueprint('performance', __name__)

@performance_bp.route('/performance/daily', methods=['GET'])
def get_daily_performance():
    db = next(get_db())
    date = request.args.get('date')

    performance_repository = PerformanceRepository(db)
    performance_service = PerformanceService(performance_repository)

    try:
        result = performance_service.get_daily_performance(db, date)
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@performance_bp.route('/performance/weekly', methods=['GET'])
def get_weekly_performance():
    db = next(get_db())
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    performance_repository = PerformanceRepository(db)
    performance_service = PerformanceService(performance_repository)

    try:
        result = performance_service.get_weekly_performance(db, start_date, end_date)
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@performance_bp.route('/performance/monthly', methods=['GET'])
def get_monthly_performance():
    db = next(get_db())
    year = int(request.args.get('year'))
    month = int(request.args.get('month'))

    performance_repository = PerformanceRepository(db)
    performance_service = PerformanceService(performance_repository)

    try:
        result = performance_service.get_monthly_performance(db, year, month)
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500