n1=int(input())
L1=[]
for i in range(n1):
    L1.append(input())
n2=int(input())
L2=[]
for j in range(n2):
    L2.append(int(input()))          
for x in range(n1):#can also use zip()
              print(L1[x],L2[x])    
                    
import array as arr
a=arr.array('i')
n=int(input())
for i in range(n):
   a.append(int(input()))
minimum=a[0]
for j in range(1,n):
   if a[j]<minimum:
      minimum=a[j]
print("Minimum element = ",minimum)

import array as arr
a1=arr.array('i')
n=int(input())
for i in range(n):
   a1.append(int(input()))
a2=arr.array('i')
n=int(input())
for i in range(n):
   a2.append(int(input()))
a3=a1+a2
l=a3.tolist()
l.sort(reverse=True)
print(*l)# '*' is used to print without brackets and commas
  


    








              
