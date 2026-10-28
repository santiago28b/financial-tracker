from dataclasses import dataclass,field,replace
from decimal import Decimal
from datetime import date
from uuid import UUID, uuid4



@dataclass(frozen=True)
class Transaction:
    account_id: UUID
    amount: Decimal
    category_id : UUID | None
    description: str
    tr_date: date = field(default_factory=date.today)
    transaction_id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        if self.amount == 0:
            raise TransactionError("amount can not be zero")
        if type(self.tr_date) != date:
            raise TransactionError("it has to be date formatted")
        if self.description == "":
            raise TransactionError("Description can't be empty")

    def assign_category(self,category_id):
        if self.category_id == category_id:
            return self
        new_obj = replace(self, category_id = category_id)
        return new_obj


class TransactionError(ValueError):
    pass


    
