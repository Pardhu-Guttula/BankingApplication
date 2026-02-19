import pytest
from app import create_application


def test_incomplete_application_handling():
    app = create_application()
    # Setup test client
    client = app.test_client()

    # Simulate incomplete application submission
    response = client.post('/submit_application', json={"name": "John Doe", "ssn": "123-45-6789"})  # Missing fields

    # Verify response
    assert response.status_code == 400
    assert response.json == {"error": "Incomplete application data"}
