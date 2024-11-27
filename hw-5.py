n=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")

n=int(input())
if n*1==0:
    print("Zero")
elif n>=0:
    print("Positive")
else:
    print("Negative")

m=int(input())
p=int(input())
c=int(input())
total=m+p+c
print(total)
percent=total/3
print(f"{percent:.2f}")
if percent>90:
    print("Eligible")
else:
    print("Not Eligible")

s=input()
if s.isupper():
    print("uppercase")
elif s.islower():
    print("lowercase")
else:
    print("combination of both")









