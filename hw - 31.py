n=int(input())
c=0
for i in range(1,n+1):
   if n%i==0:
      c+=1
if c==2:
 print("Prime number")
else:
 print("Not a prime number")
            


import math
n=int(input())
f=math.factorial(n)
print(f)


num=int(input())
n1=0
n2=1
count=0
if num<0:
    print("Enter a positive number")
elif num==1:
    print(n1)
else:
    while count<num:
       print(n1,end=" ")
       n3=n1+n2
       n1=n2
       n2=n3
       count+=1

n=int(input())
if n%11==0:
    print("It is divisible by 11")
else:
    print("It is not divisible by 11")

n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)


