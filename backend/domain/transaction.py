from dataclasses import dataclass,field
from decimal import Decimal
from datetime import date
from uuid import UUID, uuid4



@dataclass(frozen=True)
class Transaction:
    account_id: UUID
    description: str
    amount: Decimal
    date: date
    category_id : UUID | None
    transaction_id: UUID = field(default_factory=uuid4)
    
