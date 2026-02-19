import pytest
from app import create_app, db
from app.models import Interaction

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_add_interaction(client):
    response = client.post('/interactions', json={'type': 'email', 'content': 'Test interaction'})
    assert response.status_code == 201
    assert response.json['message'] == 'Interaction added successfully'

    interactions = Interaction.query.all()
    assert len(interactions) == 1
    assert interactions[0].type == 'email'
    assert interactions[0].content == 'Test interaction'


def test_get_interactions(client):
    client.post('/interactions', json={'type': 'email', 'content': 'Test interaction 1'})
    client.post('/interactions', json={'type': 'call', 'content': 'Test interaction 2'})

    response = client.get('/interactions')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['type'] == 'email'
    assert response.json[1]['type'] == 'call'