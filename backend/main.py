from domain.transaction import Transaction, TransactionError
from uuid import UUID, uuid4
from decimal import Decimal,InvalidOperation
from domain.filters import transactions_between,totals_by_category,totals_summary
from datetime import date



def transactions_menu():
    
    transactions_list = []
    summary = {}
    option = ''
    while option != 'exit':
        print("What would you like to do: \n" \
        "1: Add Transaction \n" \
        "2: total by category \n" \
        "3: summary of transactions\n")
        option = input()

        match(option):
            case '1':
                try:
                    amount = input('\namount: ')
                    description = input('description: ')
                    trans = Transaction(uuid4(),Decimal(amount),None,description)
                    print('\nYour Transaction has been recorded\n')
                    transactions_list.append(trans)
                except TransactionError as e:
                    print('something went wrong:', e)
                except InvalidOperation as e:
                    print('invalid number', e)
            case '2':
                print('Here is your totals by category: \n')
                summary = totals_by_category(transactions_list)
                print(summary)
            case '3':
                print('Here is your summary: \n')
                summary = totals_by_category(transactions_list)
                print(totals_summary(summary))

            case _:
                return "Unknown Status"


def start_tracker(): 
    user_input = ''     
    while user_input != '2':
        print('Welcome to Finace Tracker\n')
        print('Select one of the following options:\n')
        print('1: Transactions Menu')
        print('2: exit\n')
        user_input = input()

        if user_input == '1':
            transactions_menu()
        elif user_input == '2':
            break
        else:
            print('Option not available try again')

def main():             
    start_tracker() # 12 - logic


if __name__ == "__main__": #13 - glue
    main()
