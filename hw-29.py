##00 01 02
##10 11 12
##20 21 22
row=int(input())
col=int(input())
a=[]
for i in range(row):
    L=list(map(int,input().split()))
    a.append(L)
result=[]
for i in range(col):
    if i%2==0:
        for j in range(row):
            result.append(a[j][i])
    else:  
        for j in range(row-1,-1,-1):
            result.append(a[j][i])
print(' '.join(map(str,result)))


n=int(input())
m=int(input())
a=[]
for i in range(n):
    L=list(map(int,input().split()))
    a.append(L)
for i in range(n):
    l=0
    r=i
    while l<m and r>=0:
        print(a[l][r],end=" ")
        l+=1
        r-=1
    print()
for i in range(1,n):
    l=i
    r=m-1
    while l<m and r>=0:
        print(a[l][r],end=" ")
        l+=1
        r-=1
    print()
