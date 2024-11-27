grades={"ram":[99,96,89,90],"aishu":[88,90,93,87]}
student=input()
if student in grades:
    grades[student]=[100,90,80,85]
else:
    grades["anu"]=[90,89,96,84]
print(grades)
s_average=input()
avg=0
if s_average in grades:
    for i in grades[s_average]:
        avg+=i/4
    print(avg)
else:
    print("Student not exists")
r_student=input()
if r_student in grades:
    grades.pop(r_student)
    print(grades)
else:
    print("Enter a different student name")


T=tuple((50,))
print(T)
i_multiply=int(input())
print(T*i_multiply)
T=(50,100,150,200)
print(T.index(150))
L=list(T)
L[1]=200
T=tuple(L)
print(T)
S=str(T)
print(S)
maximum=max(T)
print(maximum)
minimum=min(T)
print(minimum)
count=0
for i in T:
    if i==200:
        count+=1
print(count)
N_T=((1,2,3),(4,5),(6,))
for i in N_T:
     print(i)
L=list(N_T)
L.pop(2)
N_T=tuple(L)
print(N_T)
