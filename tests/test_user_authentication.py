def test_user_login():
    assert login('user', 'password') == 'success'

def test_user_logout():
    assert logout('user') == 'success'
