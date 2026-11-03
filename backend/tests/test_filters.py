from domain.transaction import Transaction, TransactionError
from uuid import UUID, uuid4
from datetime import date
from decimal import Decimal
from domain.filters import transactions_between,totals_by_category
import pytest

def test_transaction_on_start_is_included():
    start =  date(2026, 10, 1)
    end =  date(2026, 10, 29)
    txn = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"),tr_date= date(2026,10,1),category_id='1234')     # dated on the edge
    txn_list = [txn]
    result = transactions_between(txn_list,start,end)

    assert txn in result

def test_transaction_day_before_start_is_not_included():
    start =  date(2026, 10, 1)
    end =  date(2026, 10, 29)
    txn = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"),tr_date= date(2026,9,30),category_id='1234')     # dated on the edge
    txn_list = [txn]
    result = transactions_between(txn_list,start,end)

    assert txn not in result


def test_transaction_on_last_day_to_be_included():
    start =  date(2026, 10, 1)
    end =  date(2026, 11, 1)
    txn = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"),tr_date= date(2026,10,31),category_id='1234')     # dated on the edge
    txn_list = [txn]
    result = transactions_between(txn_list,start,end)

    assert txn in result


def test_transaction_on_end_is_not_included():
    start =  date(2026, 10, 1)
    end =  date(2026, 10, 29)
    txn = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"),tr_date= date(2026,10,29),category_id='1234')     # dated on the edge
    txn_list = [txn]
    result = transactions_between(txn_list,start,end)

    assert txn not in result

def test_total_by_category_empty_list():
    txn_list = []
    result = totals_by_category(txn_list)

    assert result == {}

def test_total_by_category_one_transaction():
        txn_1 = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"),tr_date= date(2026,10,29),category_id='1234')
        txn_list = [txn_1]
        result = totals_by_category(txn_list)
        assert result == {'1234':Decimal('4.0')}
    
def test_refund_category():
        txn_1 = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("10.0"),tr_date= date(2026,10,29),category_id='1234')
        txn_2 = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("-3.0"),tr_date= date(2026,10,29),category_id='1234')
        txn_list = [txn_1,txn_2]
        result = totals_by_category(txn_list)

        assert result == {'1234':Decimal('7.0')}


     



       