import unittest
from flask import Flask, json
from main import auth_controller
from backend.authentication.services.auth_service import AuthService

class AuthControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()
        self.auth_service_mock = unittest.mock.patch('backend.authentication.services.auth_service.AuthService.authenticate')
        self.addCleanup(self.auth_service_mock.stop)
        self.mock_authenticate = self.auth_service_mock.start()

    def test_login_success(self):
        self.mock_authenticate.return_value = True
        response = self.client.post('/login', data=json.dumps({'username': 'user', 'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_credentials(self):
        self.mock_authenticate.return_value = False
        response = self.client.post('/login', data=json.dumps({'username': 'user', 'password': 'wrongpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_exception(self):
        self.mock_authenticate.side_effect = Exception('Test Exception')
        response = self.client.post('/login', data=json.dumps({'username': 'user', 'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()