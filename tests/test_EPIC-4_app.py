import pytest
from app import InteractionHistory

# Sample test data
sample_data = {
    'id': 1,
    'interaction_type': 'email',
    'interaction_details': 'Customer inquired about loan options.',
    'date': '2023-09-01'
}


def test_create_interaction():
    interaction = InteractionHistory(**sample_data)
    assert interaction.id == sample_data['id']
    assert interaction.interaction_type == sample_data['interaction_type']
    assert interaction.interaction_details == sample_data['interaction_details']
    assert interaction.date == sample_data['date']


def test_interaction_str():
    interaction = InteractionHistory(**sample_data)
    expected_str = (
        f"Interaction({sample_data['id']}, {sample_data['interaction_type']}, 
        {sample_data['interaction_details']}, {sample_data['date']})"
    )
    assert str(interaction) == expected_str
