import unittest
from flask import Flask, json
from flask.testing import FlaskClient
from main import account_lockout_controller

class AccountLockoutTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'valid_user', 'password': 'valid_pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', json.loads(response.data))

    def test_login_invalid_data(self):
        response = self.client.post('/login', data=json.dumps({'user_id': None, 'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', json.loads(response.data))

    def test_account_lockout(self):
        # Simulating account lockout scenario
        response = self.client.post('/login', data=json.dumps({'user_id': 'locked_user', 'password': 'wrong_pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 423)
        self.assertIn('error', json.loads(response.data))

    def test_login_unauthorized(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'valid_user', 'password': 'invalid_pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()