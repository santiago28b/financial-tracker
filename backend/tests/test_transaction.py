from domain.transaction import Transaction, TransactionError
from uuid import UUID, uuid4
from datetime import date
from decimal import Decimal
import pytest


def test_new_transactions_get_different_ids():
    first = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"), tr_date=date.today(), category_id='fsdfsd')
    second = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"), tr_date=date.today(), category_id='fsdfsd')
    assert first.transaction_id != second.transaction_id

def test_wrong_amount():
    with pytest.raises(ValueError):
            Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("0.0"), tr_date=date.today(), category_id='fsdfsd')

def test_wrong_date_format():
    with pytest.raises(ValueError):
            Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("5.4"), tr_date='last night', category_id='fsdfsd')

def test_transaction_no_date_passed():
          test_1 = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"),category_id='fsdfsd')
          assert test_1.tr_date == date.today()


def test_empty_description_rejected():
       with pytest.raises(TransactionError):
                   Transaction(account_id= uuid4(), description= "", amount=Decimal("4.0"), tr_date=date.today(), category_id='fsdfsd')

def test_missing_description_rejected():
       with pytest.raises(TypeError):
                   Transaction(account_id= uuid4(), amount=Decimal("4.0"), tr_date=date.today(), category_id='fsdfsd')

def test_assign_new_category_id():
        first = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"), tr_date=date.today(), category_id='1234')
        second = first.assign_category("4321")
        assert second.category_id == "4321"
        assert first.category_id == "1234"
        assert first.transaction_id == second.transaction_id

def test_assign_none_makes_uncategorised():
    first = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"), tr_date=date.today(), category_id='1234')
    second = first.assign_category(None)          # what does "uncategorised" mean? (007)
    assert second.category_id is None          # tip: compare to None with `is`

def test_assign_same_category_id():
    first = Transaction(account_id= uuid4(), description= 'ensalsa', amount=Decimal("4.0"), tr_date=date.today(), category_id='1234')
    second = first.assign_category("1234")         
    assert second is first    

       


