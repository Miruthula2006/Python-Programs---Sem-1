import math
n=int(input())
square=math.sqrt(n)
if n==int(square*square):
    print(f"{n} is a perfect square")
else:
    print(f"{n} is not a perfect square")


n1=int(input())
n2=int(input())
for i in range(n1):
    for j in range(n2):
         if i==0 or j==0 or i==n1-1 or j==n2-1:
                 print(1,end='')
         else:
                 print(0,end='')
    print()

n=int(input())
for i in range(1,n+1):
     pattern=(str(i)+'*')*(i-1)+str(i)
     print(pattern)
for i in range(n,0,-1):
     pattern=(str(i)+'*')*(i-1)+str(i)
     print(pattern)


