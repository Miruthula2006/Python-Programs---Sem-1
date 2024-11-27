n=int(input())
first=n%10
middle=int((n/10)%10)
last=int((n/100))
reverse=first*100+middle*10+last
print(f"{reverse}")


number=int(input())
a=str(number)
length=len(a)
b=int(a[0])**length+int(a[1])**length+int(a[2])**length
if number==b:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

