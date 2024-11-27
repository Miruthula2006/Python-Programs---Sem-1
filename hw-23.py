s1={9,8,7}
s2={6,7,8,9,0}
print(s1.issubset(s2))

t=(8,7,6,5,4,3,2,1)
print(t[2:6])

t=(100,10,90,80)
a,b,c,d=t
print(a)
print(b)
print(c)
print(d)


l=[(2, 5), (9, ), (8, 7, 6), (4, ), (12, 4, 16, 7)]
k=3
newl=[]
for i in l:
    if len(i)!=k:
        newl.append(i)
print(newl)
    
t=("welcome","to","heaven")
t1=""
for i in t:
    t1+=i+" "
print(t1)

lt=[('b',2),('d',4),('f',6)]
print(dict(lt))

n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
