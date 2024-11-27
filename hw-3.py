##s1={10,20,50,60}
##s2={30,40,50,60}
##s3=s1.intersection(s2)
##print("s3=",s3)
##s4=s1.symmetric_difference(s2)
##print("s4=",s4)
##s1.remove(int(input()))
##print(s1)
##
##
##t=(10,20,30,40,50)
##l=list(t)
##l.append(int(input()))
##l.append(int(input()))
##l.remove(int(input()))
##t=tuple(l)
##print(t)
##
##
##l=[]
##n=int(input())
##for i in range(n):
##    l.append(int(input()))
##print(l)
##l.sort()
##print(l)
##l.sort(reverse='True')
##print(l)
##
##
##text="     hello"
##print("rindex=",text.rindex("l"))
##print("replace=",text.replace("hello","hi"))
##print("strip=",text.strip())


n="0124456789"
for i in n:
    if i==4:
        replace=3
        n[i]=replace
print(n)
