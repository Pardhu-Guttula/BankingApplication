import pytest


def test_account_balance():
    account = Account()
    account.deposit(100)
    assert account.get_balance() == 100


def test_account_withdrawal():
    account = Account()
    account.deposit(100)
    account.withdraw(50)
    assert account.get_balance() == 50


def test_overdraft():
    account = Account()
    with pytest.raises(OverdraftError):
        account.withdraw(150)
