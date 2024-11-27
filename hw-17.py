age=int(input())
try:
    assert age>=18,'Registration error:"Participant must be atleast 18 years old"'
    assert age<=60,'Registration error:"Participant must be no older than 60 years old"'
except AssertionError as e:
    print(e)
else:
    print("Participant is eligible for registration.")

try:
    n1=int(input())
    n2=int(input())
    n3=n1+n2
    print(n3)
except ValueError as a:
    print(a)


class CustomError(Exception):
    pass
try:
    balance=int(input())
    amount=int(input())
    if amount>balance:
        raise CustomError("Insufficient Fund Error")
    elif amount<0:
        raise CustomError("Negative Withdrawal Error")
except CustomError as e:
    print(e)
else:
    newb=balance-amount
    print(f"Withdrawn Successfully.Your new balance is {newb}")


#another method
class InsufficientFundError(Exception):
    pass
class NegativeWithdrawalError(Exception):
    pass
try:
    balance=50000
    amount=int(input())
    if amount>balance:
        raise InsufficientFundError("Insufficient Fund Error")
    elif amount<0:
        raise Negative Withdrawal Error("Negative Withdrawal Error")
    else:
         newb=balance-amount
         print(f"Withdrawn Successfully.Your new balance is {newb}")
except InsufficientFundError as ife:
    print(ife)
except NegativeWithdrawalError as nwe:
    print(nwe)
        
    
    
