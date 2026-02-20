def test_new_user_registration():
    assert register_user('new_user', 'new_password') == 'user_registered'


def test_user_login_with_wrong_password():
    assert login('user', 'wrong_password') == 'login_failed'
