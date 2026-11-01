from domain.transaction import Transaction
from datetime import date



def transactions_between(transaction_list:list[Transaction], start_date:date,end_date:date)-> list[Transaction]:
    transactions = []
    for transaction in transaction_list:
        if start_date <= transaction.tr_date < end_date:
            transactions.append(transaction)

    return transactions

def totals_by_category(txns: list[Transaction]) -> dict:
    if len(txns) == 0:
        return {}
    pass