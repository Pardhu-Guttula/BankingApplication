# Epic Title: Monitor user behavior metrics

import logging
from flask import Blueprint, jsonify
from backend.analytics.repositories.user_behavior_repository import UserBehaviorRepository

behavior_bp = Blueprint('behavior', __name__)
behavior_repository = UserBehaviorRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@behavior_bp.route('/user/session-duration', methods=['GET'])
def get_session_duration():
    average_duration = behavior_repository.get_average_session_duration()
    return jsonify({'average_session_duration': average_duration}), 200

@behavior_bp.route('/user/page-views', methods=['GET'])
def get_page_views():
    total_views = behavior_repository.get_total_page_views()
    return jsonify({'total_page_views': total_views}), 200

@behavior_bp.route('/user/click-through-rates', methods=['GET'])
def get_click_rates():
    click_rates = behavior_repository.get_click_through_rates()
    return jsonify({'click_through_rates': click_rates}), 200