import pytest
from app import create_application

def test_incomplete_application_handling():
    app = create_application()
    with app.test_client() as client:
        response = client.post('/apply', json={})  # Posting an empty JSON to simulate incomplete application
        assert response.status_code == 400
        assert response.json == {'error': 'Incomplete application data'}
