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
One movement of money on a date, with an amount and a description, belonging to one Account.
_Avoid_: Expense, record, entry

**DB transaction**:
A group of database writes that commit or roll back together. Always written with the "DB" prefix.
_Avoid_: Transaction (unqualified)
