##def quiz():
##    questions = {
##        "What is the capital of India?": "Delhi",
##        "What is 2 + 2?": "4",
##        "What is the largest ocean on Earth?": "Pacific Ocean",
##        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
##        "What is the chemical symbol for water?": "H2O"}
##    
##    score=0
##    print("Welcome to the Quiz!")
##    for question,answer in questions.items():
##        ans=input(f"{question} ")
##        if ans.upper()==answer.upper():
##            print("Correct!")
##            score+=1
##        else:
##            print(f"Wrong! The correct answer is {answer}.")
##    
##    print(f"Your score is {score}")
##quiz()
##
##
##
def deposit(account, amount):
    accounts[account]['balance']+= amount
    print("deposited successfully.")

def withdraw(account, amount):
    if amount > accounts[account]['balance']:
        print("Insufficient balance! Unable to withdraw.")
    else:
        accounts[account]['balance'] -= amount
        print("withdrawn successfully.")

def check_balance(account):
    print(f"Current balance for {account}: {accounts[account]['balance']}.")



accounts = {
    'Sam': {'balance': 5000},
    'Bob': {'balance': 3000},
    'Anu': {'balance': 7000}
}

def banking_chatbot():
    print("Welcome to the Banking Chatbot!")
    
    while True:
        print("Available Accounts")
        for i in accounts:
            print(i)
        account=input()
        
        if account.lower()=='exit':
            print("Thank you for using the Banking Chatbot! Goodbye!")
            break
        elif account not in accounts:
            print("Account not found! Please try again.")
            continue
        
        while True:
            print("\n--- Banking Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            option = int(input())

            if option == 1:
                amount = float(input("Enter amount to deposit: "))
                deposit(account, amount)
            elif option == 2:
                amount = float(input("Enter amount to withdraw: "))
                withdraw(account, amount)
            elif option == 3:
                check_balance(account)
            elif option == 4:
                print("Thank you for using the Banking Chatbot! Goodbye!")
                quit()
            else:
                print("Invalid option! Please try again.")

banking_chatbot()
