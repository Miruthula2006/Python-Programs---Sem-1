n=int(input())
b=0
num=n
while n>0:
    a=n%10
    b+=a
    n//=10
if num%b==0:
    print(f"{num} is a Harshad Number")
else:
    print(f"{num} is not a Harshad Number")



n=int(input())
L=[]
for i in range(n):
    L.append(int(input()))
print(L)
books=[int(num) for num in L]
total=sum(books)
print(total)


n=int(input())
for i in range(1,n+1):
    print("*"*i)


