import pytest
from backend.app import create_account, delete_account, get_account_balance


def test_create_account():
    account_id = create_account("John Doe", 500)
    assert account_id is not None


def test_delete_account():
    account_id = create_account("Jane Doe", 1000)
    result = delete_account(account_id)
    assert result is True


def test_get_account_balance():
    account_id = create_account("Alice Smith", 1500)
    balance = get_account_balance(account_id)
    assert balance == 1500
