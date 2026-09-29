def process_info(expense,amount):
    id = len(transactions)
    transactions.append(id+1,expense,amount)

def start_tracker():
    while input != 'exit':
        new_expense = input('What is your expense: ')
        amount = int(input('input amount: '))

        process_info(new_expense,amount)
        print('your new expense ', new_expense, ' has been recorded ', 'the amount is $',amount)
        process_info()
    



def main():
    transactions = []
    start_tracker()


if __name__ == "__main__":
    main()
