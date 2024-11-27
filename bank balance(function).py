def withdraw(w):
    global balance
    balance-=w
    print("Withdrawn successfully.Go back to the main menu to view balance")
def deposit(d):
    global balance
    balance+=d
    print("Deposited successfully...")
def checkbalance():
    print("Balance is",balance)
def end_transaction():
    quit()

balance=20000
while True:
    print("1.Withdraw\n2.Deposit\n3.Balance\n4.Exit")
    option=int(input("Enter the operation to proceed..."))
    match option:
        case 1:
            draw=int(input())
            withdraw(draw)
        case 2:
            dep=int(input())
            deposit(dep)
        case 3:
            checkbalance()
        case 4:
            end_transaction()
        case _:
            print("Enter any valid option")
        
        
