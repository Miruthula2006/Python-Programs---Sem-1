x=int(input())
a=0
b=1
even_count=0
while even_count<x:
    a,b=b,a+b      
    if b%2==0: 
        even_count+=1
print(b)

import math
num_of_plots=int(input())
area=list(map(int,input().split()))
count=0
for i in area:
    square=int(math.sqrt(i))
    if i==square*square:
        count+=1
print(count)

##another method for 1
##x=int(input())
##a=0
##b=1
##even_count=0
##while even_count<x:
##    c=a+b
##    a=b
##    b=c
##    if b%2==0:
##        even_count+=1
##print(b)
        
             




