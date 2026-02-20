import pytest
from app import some_function

def test_some_function():
    # Arrange
    input_value = 'test input'
    expected_output = 'expected output'
    
    # Act
    result = some_function(input_value)
    
    # Assert
    assert result == expected_output
