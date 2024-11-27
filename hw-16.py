try:
   string=input()
   substring=input()
   print(string.index(substring))
except Exception as x:
   print("substring was not found")


try:
    L=list(map(int,input().split()))
    length=len(L)
    total=sum(L)
    average=total/length
    print(average)
except ZeroDivisionError as y:
    print("List can't be empty")
    

try:
    t=("fruits","vegetables","meat")
    print(t[int(input())])
except IndexError as z:
    print(z)





