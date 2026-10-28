# Finance Tracker

A personal finance app that answers one question well: where did my money go last month?

## Language

**User**:
The person who signs in and owns all other data.
_Avoid_: Account (for the person), customer

**Account**:
A place money lives: a checking account, a savings account or a credit card.
_Avoid_: User account, login

**Transaction**:
One movement of money on a date, with a non-zero amount and a required, non-empty description, belonging to one Account. Invalid data raises TransactionError when the Transaction is created.
_Avoid_: Expense, record, entry

**Category**:
A label a User puts on Transactions, owned by that User; defaults are copied to each User at sign-up.
_Avoid_: Tag, type

**Uncategorised**:
A Transaction whose `category_id` is None: no Category assigned yet, or its Category was deleted (DECISIONS 007).
_Avoid_: Other, misc (those would be real Categories)

**Reassigning a category**:
Giving a Transaction a different `category_id` (or None). Transactions are frozen, so this returns a new Transaction with the same transaction_id; the original is unchanged.
_Avoid_: Updating, editing the Transaction

**Amount**:
A Transaction's money value, exact to the cent: Decimal in Python, Numeric with scale 2 in Postgres. Never a float.
_Avoid_: Price, value

**Transaction date**:
The calendar day a Transaction happened, stored as a date with no time or timezone. Defaults to today when not given. Field name: `tr_date`.
_Avoid_: Timestamp, datetime

**Opening balance**:
The Transaction that records the money already in an Account when the User starts tracking it.
_Avoid_: Starting balance column

**Archived account**:
An Account the User has closed: hidden by setting archive_at, never deleted, so its Transactions stay. A real DELETE only happens when the whole User is removed.
_Avoid_: Deleted account

**Transfer**:
Money moved between two of a User's own Accounts: two Transactions (−X and +X) that point at each other via counterpart_transaction_id. Not spending.
_Avoid_: Transfer flag, is_transfer

**DB transaction**:
A group of database writes that commit or roll back together. Always written with the "DB" prefix.
_Avoid_: Transaction (unqualified)
