# File: tests/test_roles.py
import unittest
from some_module import Role, create_role, get_role_by_id, delete_role, update_role

class TestRoles(unittest.TestCase):
    def test_create_role_success(self):
        role = create_role(name="Admin", permissions={"read": True, "write": True})
        self.assertIsNotNone(role)
        self.assertEqual(role.name, "Admin")
        self.assertEqual(role.permissions, {"read": True, "write": True})

    def test_create_role_empty_name(self):
        with self.assertRaises(ValueError):
            create_role(name="", permissions={"read": True, "write": True})

    def test_create_role_null_permissions(self):
        with self.assertRaises(TypeError):
            create_role(name="Admin", permissions=None)

    def test_get_role_by_id_success(self):
        role = create_role(name="Admin", permissions={"read": True, "write": True})
        fetched_role = get_role_by_id(role.role_id)
        self.assertEqual(fetched_role.name, "Admin")
        self.assertEqual(fetched_role.permissions, {"read": True, "write": True})

    def test_get_role_by_id_not_found(self):
        self.assertIsNone(get_role_by_id(999))

    def test_delete_role_success(self):
        role = create_role(name="Admin", permissions={"read": True, "write": True})
        delete_role(role.role_id)
        self.assertIsNone(get_role_by_id(role.role_id))

    def test_delete_role_not_found(self):
        with self.assertRaises(ValueError):
            delete_role(999)
    
    def test_update_role_success(self):
        role = create_role(name="Admin", permissions={"read": True, "write": True})
        updated_role = update_role(role.role_id, name="SuperAdmin", permissions={"read": True, "write": True, "delete": True})
        self.assertEqual(updated_role.name, "SuperAdmin")
        self.assertEqual(updated_role.permissions, {"read": True, "write": True, "delete": True})

    def test_update_role_not_found(self):
        with self.assertRaises(ValueError):
            update_role(999, name="SuperAdmin", permissions={"read": True, "write": True, "delete": True})

    def test_update_role_empty_name(self):
        role = create_role(name="Admin", permissions={"read": True, "write": True})
        with self.assertRaises(ValueError):
            update_role(role.role_id, name="", permissions={"read": True, "write": True, "delete": True})

    def test_update_role_null_permissions(self):
        role = create_role(name="Admin", permissions={"read": True, "write": True})
        with self.assertRaises(TypeError):
            update_role(role.role_id, name="SuperAdmin", permissions=None)

if __name__ == '__main__':
    unittest.main()