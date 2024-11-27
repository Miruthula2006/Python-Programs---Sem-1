b=int(input())
if b>0:
   print("sufficient")
   while True:
       print("1.Deposit\n2.Withdraw\n3.View Balance\n4.Exit")
       option=int(input())
       if option==1:
          deposit=int(input())
          b+=deposit
          print("After deposit the balance: ",b)
       elif option==2:
          Withdraw=int(input())
          b-=Withdraw
          print("After withdraw the balance: ",b)
       elif option==3:
          print("Balance: ",b)
       elif option==4:
          quit()
       else:
          print("Invalid option")
else:
    print("Not sufficient")

restaurant_name=input()
print("1.Biryani\n2.Dessert\n3.Starters")
while True:
    choice=int(input())
    if choice==1:
        print("Chicken Biryani --> Rs.120")
        print("Mutton Biryani --> Rs.200")
        print("Veg Biryani --> Rs.100")
    elif choice==2:
        print("Ice cream --> Rs.140")
        print("Jamun --> Rs.90")
        print("Falooda --> Rs.150")
    elif choice==3:
        print("Chicken 65 --> Rs.250")
        print("Fish finger --> Rs.300")
        print("Lollipop --> Rs.260")
    elif choice==4:
        quit()
    else:
        print("Sorry Not Available")
        
