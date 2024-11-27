start=int(input())
end=int(input())
print("Odd numbers:")
for num in range(start, end+1):
   if num%2!=0:
       print(num, end=' ')
print()
print("Even numbers:")
for num in range(start, end+1):
   if num%2==0:
       print(num,end=' ')
print()


txt=input()
for x in range(len(txt)-1,-1,-1):
   z=txt[x]
   print(z.upper(),end=" ")


sale_figures=[150, -20, 300, -50, 200, -10, 400, -30]
positive=0
negative=0
for x in sale_figures:
    if x>0:
       positive+=1
    elif x<0:
       negative-=1
print("Number of successful sales:",positive)
print("Number of returns or losses:",negative)


