n=4
a=65
for i in range(n):
    for j in range(i+1):
        print(chr(a),end=" ")
        a+=1
    print()

x=3
for i in range(x):
    if x<=8:
        print(x*10)
        x+=2

for x in range(10,20):
  if x%2==0:
     continue
  print(x)

O/P:
11
13
15
17
19

import array as arr
a=arr.array('i')
n=int(input())
for k in range(n):
    a.append(int(input()))
duplicate=[]
for i in range(n):
     for j in range(i+1,n):
       if a[j]==a[i]:
           duplicate.append(a[i])
print(duplicate)

#1
import array as arr
a=arr.array('i')
n=int(input())
for k in range(n):
   a.append(int(input()))
negative=[]
positive=[]
for i in a:
    if i<0:
        negative.append(i)
    else:
        positive.append(i)
a1=negative+positive
print(a1)

#1
n=int(input())#4
a=[]
for i in range(n):
    a.append(int(input()))#2 -8 7 -7
j=o
for i in range(0,n):
    if (a[i]<0):
        t=a[i]
        a[i]=a[j]
        a[j]=t
        j=j+1
print(a)#-8 -7 7 2


           

    
