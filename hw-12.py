 num=int(input())
sum_digit=0
while num!=0:
    rem=num%10
    sum_digit+=rem
    num//=10
print(f"{sum_digit}")


num=int(input())
product=1
while num!=0:
    rem=num%10
    product*=rem
    num//=10
print(f"{product}")



n=int(input())
for i in range(n,0,-1):
    print(i)
