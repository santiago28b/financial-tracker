from domain.transaction import Transaction
from datetime import date
from decimal import Decimal,ROUND_HALF_UP
from uuid import UUID, uuid4




def transactions_between(transaction_list:list[Transaction], start_date:date,end_date:date)-> list[Transaction]:
    transactions = []
    for transaction in transaction_list:
        if start_date <= transaction.tr_date < end_date:
            transactions.append(transaction)

    return transactions

def totals_by_category(txns: list[Transaction]) -> dict:
    totals_by_cat = {}
    for transaction in txns:
         totals_by_cat[transaction.category_id] = totals_by_cat.get(transaction.category_id,0) + transaction.amount

    return totals_by_cat

def totals_summary(totals: dict[UUID | None,Decimal]) -> list[tuple[UUID|None,Decimal,Decimal]]:
    summary = []
    if not totals:
            return summary
    total = sum([amount for amount in totals.values()])
    for key,val in totals.items():
        percentage = (val/total) * Decimal('100')
        summary.append((key,val,percentage.quantize(Decimal('0.01'),rounding = ROUND_HALF_UP)))

    shortage = 100 - sum(percentage for _,_, percentage in summary)
    sorted_summary = sorted(summary, key=lambda pair:pair[2],reverse=True)

    old_tuple = sorted_summary[0]
    sorted_summary[0] = (old_tuple[0],old_tuple[1],old_tuple[2]+shortage)

    return sorted_summary