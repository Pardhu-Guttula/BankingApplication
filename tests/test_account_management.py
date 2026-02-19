import pytest
from app import create_app, db
from app.models import User, Account

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client  # this is where the testing happens!

    with flask_app.app_context():
        db.drop_all()


def test_account_creation(test_client):
    # Assuming there is a User model with an id of 1 already present
    response = test_client.post('/create_account', json={
        'user_id': 1,
        'account_type': 'savings',
        'balance': 1000
    })

    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['message'] == 'Account created successfully.'

    # Query the database to check if the account was created
    account = Account.query.filter_by(user_id=1).first()
    assert account is not None
    assert account.account_type == 'savings'
    assert account.balance == 1000


def test_account_creation_missing_user(test_client):
    # Trying to create an account for a non-existent user
    response = test_client.post('/create_account', json={
        'user_id': 999,  # Assuming there is no user with id 999
        'account_type': 'savings',
        'balance': 1000
    })

    assert response.status_code == 400
    json_data = response.get_json()
    assert json_data['message'] == 'User not found.'


def test_account_deletion(test_client):
    # Assuming there is an Account model with an id of 1
    response = test_client.delete('/delete_account', json={
        'account_id': 1
    })

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Account deleted successfully.'

    # Query the database to check if the account was deleted
    account = Account.query.filter_by(id=1).first()
    assert account is None
