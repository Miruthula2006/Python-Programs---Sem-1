def square():
    n=int(input())
    s=n*n
    return s
sqr=square()
print("Square of the number is ",sqr)

def name(first_name,last_name):
    print(first_name,last_name)
first_name=input()
last_name=input()
name(first_name,last_name)

def product(n1,n2):
    p=n1*n2
    return p
n1=int(input())
n2=int(input())
pro=product(n1,n2)
print("Product = ",pro)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
n=int(input())
factorial(n)

def lst():
    n=int(input())
    l=list(map(int,input().split()))
    return l
L=lst()
print(L)
    
        
        
