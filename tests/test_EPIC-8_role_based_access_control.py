import pytest

class TestRoleBasedAccessControl:

    def test_admin_access(self):
        user_role = 'admin'
        assert self.has_access(user_role) == True

    def test_user_access(self):
        user_role = 'user'
        assert self.has_access(user_role) == True

    def test_guest_access(self):
        user_role = 'guest'
        assert self.has_access(user_role) == False

    def has_access(self, role):
        if role == 'admin':
            return True
        elif role == 'user':
            return True
        elif role == 'guest':
            return False
        return False
