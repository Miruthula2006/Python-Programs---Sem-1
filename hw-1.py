L=[12,34,56,67]
L.append(90)
print("After adding 90 = ",L)
L.remove(56)
print("After removing 56 = ",L)

age=int(input())
print(f"You are {'Eligible' if age>=24 else 'Not Eligible'}")

name=input()
number=int(input())
balance=float(input())
print(f"Account Name: {name}")
print(f"Account Number: {number}")
print(f"Balance: {balance:.2f}")

L=[3,6,8,12,15]
L.remove(8)
L.insert(2,9)
print(L)
