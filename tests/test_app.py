import pytest
from app import create_account, delete_account, get_account_details


def test_create_account():
    account_id = create_account('John Doe', 1000)
    assert account_id is not None


def test_delete_account():
    account_id = create_account('Jane Doe', 2000)
    delete_account(account_id)
    assert get_account_details(account_id) is None


def test_get_account_details():
    account_id = create_account('Alice', 3000)
    account_details = get_account_details(account_id)
    assert account_details is not None
    assert account_details['balance'] == 3000
