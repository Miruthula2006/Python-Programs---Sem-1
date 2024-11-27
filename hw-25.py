n=int(input())
a=[]
total=0
for i in range(n):
    L=list(map(int,input().split()))
    a.append(L)
print(a)
for j in a:
    total+=sum(j)
print("Total sales = ",total) 


n=int(input())
a=[]
for i in range(n):
    L=list(map(int,input().split()))
    a.append(L)
e=int(input("Enter the element to be found: "))
f=False
for i in range(n):
    for j in range(n):
        if a[i][j]==e:
             print(f"Found at {i},{j}")
             f=True
             break
if not f:
    print("Not Found")


n=int(input())
arr=[]
for i in range(n):
    L=list(map(int,input().split()))
    arr.append(L)
print("Original matrix:")
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
print("Transpose of the matrix:")
for i in range(n):
    for j in range(n):
        print(arr[j][i],end=" ")
    print()


n=int(input())
seats=[]
total=0
for i in range(n):
    L=list(map(int,input().split()))
    seats.append(L)
print("Theater Seating Chart:")
for i in seats:
    for j in i:
        if j==0:
            print("O",end=" ")
        else:
            print("X",end=" ")
    print()

