# Updated Unit Test Code for User Authentication and Security
import unittest
from flask import Flask, json
from backend.authentication.services.auth_service import AuthService
from backend.authentication.controllers.auth_controller import auth_controller

class AuthControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        AuthService.authenticate = lambda self, u, p: True
        response = self.client.post('/login', data=json.dumps({
            "username": "valid_user",
            "password": "valid_pass"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Login successful"})

    def test_login_invalid_credentials(self):
        AuthService.authenticate = lambda self, u, p: False
        response = self.client.post('/login', data=json.dumps({
            "username": "invalid_user",
            "password": "invalid_pass"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid credentials"})

    def test_login_missing_username(self):
        data = {"password": "valid_pass"}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message": "Username required"})

    def test_login_missing_password(self):
        data = {"username": "valid_user"}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message": "Password required"})

    def test_login_exception_handling(self):
        AuthService.authenticate = lambda self, u, p: (_ for _ in ()).throw(Exception('Test Exception'))
        response = self.client.post('/login', data=json.dumps({
            "username": "valid_user",
            "password": "valid_pass"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Login failed"})

if __name__ == '__main__':
    unittest.main()