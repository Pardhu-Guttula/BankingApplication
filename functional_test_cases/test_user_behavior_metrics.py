import pytest
from flask import Flask
from backend.analytics.controllers.user_behavior_controller import behavior_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(behavior_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test for getting session duration

def test_get_session_duration_success(client, mocker):
    mocker.patch('backend.analytics.repositories.user_behavior_repository.UserBehaviorRepository.get_average_session_duration', return_value=120.0)
    response = client.get('/user/session-duration')
    assert response.status_code == 200
    assert response.json == {'average_session_duration': 120.0}

def test_get_session_duration_failure(client, mocker):
    mocker.patch('backend.analytics.repositories.user_behavior_repository.UserBehaviorRepository.get_average_session_duration', side_effect=Exception("Unable to process your request"))
    response = client.get('/user/session-duration')
    assert response.status_code == 500
    assert response.json == {'error': 'Unable to process your request'}

# Test for getting page views

def test_get_page_views_success(client, mocker):
    mocker.patch('backend.analytics.repositories.user_behavior_repository.UserBehaviorRepository.get_total_page_views', return_value=50)
    response = client.get('/user/page-views')
    assert response.status_code == 200
    assert response.json == {'total_page_views': 50}

def test_get_page_views_failure(client, mocker):
    mocker.patch('backend.analytics.repositories.user_behavior_repository.UserBehaviorRepository.get_total_page_views', side_effect=Exception("Unable to process your request"))
    response = client.get('/user/page-views')
    assert response.status_code == 500
    assert response.json == {'error': 'Unable to process your request'}

# Test for getting click through rates

def test_get_click_rates_success(client, mocker):
    mocker.patch('backend.analytics.repositories.user_behavior_repository.UserBehaviorRepository.get_click_through_rates', return_value=[{'element_id': 'btn_1', 'total_clicks': 10}])
    response = client.get('/user/click-through-rates')
    assert response.status_code == 200
    assert response.json == {'click_through_rates': [{'element_id': 'btn_1', 'total_clicks': 10}]}

def test_get_click_rates_failure(client, mocker):
    mocker.patch('backend.analytics.repositories.user_behavior_repository.UserBehaviorRepository.get_click_through_rates', side_effect=Exception("Unable to process your request"))
    response = client.get('/user/click-through-rates')
    assert response.status_code == 500
    assert response.json == {'error': 'Unable to process your request'}
