num1=int(input())
num2=int(input())
print(f"{num1 if num1<num2 else num2}")


p=float(input())#principal amount
r=float(input())#rate of interest
n=float(input())#time
#compound interest formula=CI= P(1 + r/100)**n-p
ci=p*((1+r/100)**n)-p
print(ci)


a=int(input())       8 4 2 1
b=int(input())   3   0 0 1 1
c=a<<1           6   0 1 1 0
d=b>>1          3<<1 0 1 1 0 = 6
print(c,d)      6>>1 0 0 1 1 = 3 

n=int(input())
L=[]
for i in range(n):
    L.append(input())
print(L)
x=input() in L
print(x)
y=input() not in L
print(y)

S={"Example for membership operator"}
if "the" not in S:
    print("True")
else:
    print("False")









