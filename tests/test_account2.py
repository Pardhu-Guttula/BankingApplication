import pytest


def test_account_balance_epic2():
    account = Account()
    account.deposit(200)
    assert account.get_balance() == 200


def test_account_withdrawal_epic2():
    account = Account()
    account.deposit(200)
    account.withdraw(100)
    assert account.get_balance() == 100


def test_overdraft_epic2():
    account = Account()
    with pytest.raises(OverdraftError):
        account.withdraw(300)
