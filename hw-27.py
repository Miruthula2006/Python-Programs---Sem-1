n=int(input())
a=[]
for i in range(n):
    L=list(map(int,input().split()))
    a.append(L)
average=[]
for i in range(n):
    s=sum(a[i])
    avg=s/3
    average.append(avg)
print("Average grades for each student: ")
for i in range(n):
    print(f"Student {i + 1}: {average[i]:.2f}")
subject=["Math","Science","English"]
m=[]
for i in range(3):
    max=a[0][i]
    for j in range(1,n):
        if a[j][i]>max:
            max=a[j][i]
    m.append(max)
print("Highest grade in each subject:")
for i in range(3):
    print(f"{subject[i]}: {m[i]}")
overall_avg=sum(average)/len(average)
print(f"Overall class average: {overall_avg:.2f}")



n=int(input())
a=[]
for i in range(n):
    L=list(map(int,input().split()))
    a.append(L)
quantities=[]
for i in range(n):
    s=sum(a[i])
    quantities.append(s)
print("Total quantities of each product: ")
for i in range(n):
    print(f"Product {i+1}: {quantities[i]}")
product3=a[2]
high_quan=max(product3)
position=product3.index(high_quan)
section=["A","B","C","D"]
print(f"Section with the highest quantity for Product 3: Section {section[position]}") 
low=min(quantities)
low_index=quantities.index(low)
print(f"Product with the lowest total quantity: Product {low_index+1}")
    



    

