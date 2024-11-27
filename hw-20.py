for n in range(100,500):
    if n%11==0 and n%2!=0:
        print(n)


n=4
for i in range(n+1):  # 1,2,3,4
    for j in range(1,i+1): #  1   1 2   1 2 3  1 2 3 4
        print(j,end=" ")
    print()

x=8
while x<=20:
 print(x**2)
 x+=3
O/P:
64
121
196
289
400


for i in "Python":
 print(i,'?$')
O/P:
P ?$
y ?$
t ?$
h ?$
o ?$
n ?$


for i in "Python":
 print(i,end=" ")
O/P:
P y t h o n 


for i in range(5,9):
 print(i)
O/P:
5
6
7
8

n=int(input())
if n<2:
    f=False
else:
    f=True
    for i in range(2,n+1):
        if n%i==0:
            f=False
            break
        if f:
            print("Prime number")
        else:
            print("Not a Prime Number")

n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

num=int(input())
product=1
while num!=0:
    rem=num%10
    product*=rem
    num//=10
print(f"{product}")

import math
n=int(input())
s=1
for x in range(1,n+1):
    s+=x*x/math.factorial(x)
print(s)    
                                   
n=int(input())
s=str(n)
p=s[::-1]
if p==s:
    print("Palindrome")
else:
    print("Not a Palindrome")

n=int(input())  
fact=1 
for i in range(1,n+1):  
    fact*=i
print(fact)
