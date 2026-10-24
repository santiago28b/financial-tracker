def process_info(expense,amount):  # 1 - I/O glue
    id = len(transactions) #2 - logic 
    transactions.append(id+1,expense,amount) #3 - logic

def start_tracker():      
    while input != 'exit': #4- I/O
        new_expense = input('What is your expense: ') #5 I/O
        amount = int(input('input amount: ')) #6 logic

        process_info(new_expense,amount) #7 - Glue
        print('your new expense ', new_expense, ' has been recorded ', 'the amount is $',amount) #8 I/O + logic
        process_info() #9 - logic and glue
    



def main():             # 10 - glue
    transactions = [] # 11 - logic
    start_tracker() # 12 - logic


if __name__ == "__main__": #13 - glue
    main()
