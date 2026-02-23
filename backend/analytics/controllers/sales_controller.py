# Epic Title: Track Sales Performance Metrics

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.analytics.repositories.sales_repository import SalesRepository
from backend.analytics.services.sales_service import SalesService

sales_bp = Blueprint('sales', __name__)

@sales_bp.route('/sales/daily', methods=['GET'])
def get_daily_sales():
    db = next(get_db())
    date = request.args.get('date')

    sales_repository = SalesRepository(db)
    sales_service = SalesService(sales_repository)

    try:
        result = sales_service.get_daily_sales(db, date)
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@sales_bp.route('/sales/weekly', methods=['GET'])
def get_weekly_sales():
    db = next(get_db())
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    sales_repository = SalesRepository(db)
    sales_service = SalesService(sales_repository)

    try:
        result = sales_service.get_weekly_sales(db, start_date, end_date)
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500

@sales_bp.route('/sales/monthly', methods=['GET'])
def get_monthly_sales():
    db = next(get_db())
    year = int(request.args.get('year'))
    month = int(request.args.get('month'))

    sales_repository = SalesRepository(db)
    sales_service = SalesService(sales_repository)

    try:
        result = sales_service.get_monthly_sales(db, year, month)
        return jsonify(result), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500