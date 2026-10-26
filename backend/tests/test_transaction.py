from domain.transaction import Transaction
from uuid import UUID, uuid4
from datetime import date


def test_new_transactions_get_different_ids():
    first = Transaction(account_id= uuid4(), description= 'ensalsa', amount=4, date=date.today(), category_id='fsdfsd')
    second = Transaction(account_id= uuid4(), description= 'ensalsa', amount=4, date=date.today(), category_id='fsdfsd')
    assert first.transaction_id != second.transaction_id