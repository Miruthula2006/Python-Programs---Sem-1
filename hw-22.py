ld={"sam":1234,"neha":5678}
name=input()
password=int(input())
if name not in ld:
    print("Invalid username")
elif password!=ld[name]:
    print("Incorrect password")
else:
    print("Sucessfully logged in")

number=int(input())
num=str(number)
to_replace=int(input())
replace_with=int(input())
new=0
for i in num:
    if str(i) in str(to_replace):
        i=replace_with
    print(i,end="")

n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
k=sorted(a)
print(k[1])

n=int(input())
a=list(map(int,input().split()))
m=int(input())
count=a.count(m)
if count>n/2:
    print(f"{count} is a majority element.")
else:
    print(f"{count} is not a majority element.")


    

     



        
        
    
    


        
    
