"""
m,n=map(int,input().split())
a1=[]
for i in range(m):
    L=list(map(int,input().split()))
    a1.append(L)
a2=[]
for i in range(n):
    L=list(map(int,input().split()))
    a2.append(L)
for i in range(n):
    for j in range(n):
        s=a1[i][j]+a2[i][j]
        print(s,end=" ")
    print()

"""
n=int(input())
arr=[]
for i in range(n):
    L=list(map(int,input().split()))
    arr.append(L)
transpose=[[arr[j][i] for j in range(n)] for i in range(n)]
print(transpose)
for i in transpose:
    i.reverse()
for i in range(n):
    for j in range(n):
        print(transpose[i][j],end=" ")
    print()


r,c=map(int,input().split())
a1=[]
for i in range(r):
    L=list(map(int,input().split()))
    a1.append(L)
m=a1[0][0]
for i in a1:
    for j in i:
       if j>m:
          m=j
print("Maximum element =",m)


r,c=map(int,input().split())
a=[]
for i in range(r):
    L=list(map(int,input().split()))
    a.append(L)
f=True
for i in range(r):
    for j in range(c):
        if a[i][j]!=a[j][i]:
            f=False
            break
if f:
    print("Symmetric matrix")
else:
    print("Not a Symmetric matrix")
        





