import pytest
from app import process_application

def test_incomplete_application_missing_fields():
    application_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
        # Missing other fields like address, phone number
    }
    result = process_application(application_data)
    assert result == "Incomplete application", "Fails if all necessary fields are not provided"

def test_incomplete_application_empty_fields():
    application_data = {
        "first_name": "",
        "last_name": "",
        "email": ""
        # Empty fields provided
    }
    result = process_application(application_data)
    assert result == "Incomplete application", "Fails if necessary fields are empty"