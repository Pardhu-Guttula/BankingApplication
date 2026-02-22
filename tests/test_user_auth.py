# File: tests/test_user_auth.py

import unittest
from user_auth import Users

class TestUserAuth(unittest.TestCase):
    def setUp(self):
        self.users = Users()

    def test_create_user_success(self):
        result = self.users.create_user('John Doe', 'john.doe@example.com', 1)
        self.assertEqual(result['status'], 'success')
        self.assertIsNotNone(result['user_id'])

    def test_create_user_duplicate_email(self):
        self.users.create_user('Jane Doe', 'jane.doe@example.com', 1)
        result = self.users.create_user('Jane Roe', 'jane.doe@example.com', 1)
        self.assertEqual(result['status'], 'error')
        self.assertIn('email already exists', result['message'])

    def test_create_user_invalid_email(self):
        result = self.users.create_user('Jane Doe', 'not-an-email', 1)
        self.assertEqual(result['status'], 'error')
        self.assertIn('invalid email', result['message'])

    def test_create_user_missing_name(self):
        result = self.users.create_user('', 'john.doe@example.com', 1)
        self.assertEqual(result['status'], 'error')
        self.assertIn('name is required', result['message'])

    def test_create_user_missing_email(self):
        result = self.users.create_user('John Doe', '', 1)
        self.assertEqual(result['status'], 'error')
        self.assertIn('email is required', result['message'])

    def test_create_user_nonexistent_role(self):
        result = self.users.create_user('John Doe', 'john.doe@example.com', 99)
        self.assertEqual(result['status'], 'error')
        self.assertIn('role does not exist', result['message'])

    def test_get_user_success(self):
        user_id = self.users.create_user('John Doe', 'john.doe@example.com', 1)['user_id']
        user = self.users.get_user(user_id)
        self.assertEqual(user['name'], 'John Doe')
        self.assertEqual(user['email'], 'john.doe@example.com')

    def test_get_user_not_found(self):
        result = self.users.get_user(999)
        self.assertIsNone(result)

    def test_delete_user_success(self):
        user_id = self.users.create_user('John Doe', 'john.doe@example.com', 1)['user_id']
        result = self.users.delete_user(user_id)
        self.assertEqual(result['status'], 'success')
        user = self.users.get_user(user_id)
        self.assertIsNone(user)

    def test_delete_user_not_found(self):
        result = self.users.delete_user(999)
        self.assertEqual(result['status'], 'error')
        self.assertIn('user not found', result['message'])

    def test_update_user_success(self):
        user_id = self.users.create_user('John Doe', 'john.doe@example.com', 1)['user_id']
        result = self.users.update_user(user_id, 'Johnny Doe', 'johnny.doe@example.com', 2)
        self.assertEqual(result['status'], 'success')
        user = self.users.get_user(user_id)
        self.assertEqual(user['name'], 'Johnny Doe')
        self.assertEqual(user['email'], 'johnny.doe@example.com')

    def test_update_user_not_found(self):
        result = self.users.update_user(999, 'Johnny Doe', 'johnny.doe@example.com', 2)
        self.assertEqual(result['status'], 'error')
        self.assertIn('user not found', result['message'])

    def test_update_user_duplicate_email(self):
        self.users.create_user('Jane Doe', 'jane.doe@example.com', 1)
        user_id = self.users.create_user('John Doe', 'john.doe@example.com', 1)['user_id']
        result = self.users.update_user(user_id, 'Johnny Doe', 'jane.doe@example.com', 2)
        self.assertEqual(result['status'], 'error')
        self.assertIn('email already exists', result['message'])

if __name__ == '__main__':
    unittest.main()