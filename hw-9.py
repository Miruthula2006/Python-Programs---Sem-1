marks=[85,90,-5,76,92,-1,88,79,55]
for j in marks:
   if j==-1:
      print("Encountered missing data.stopping processing")
      break
   elif j<-1:
      print(f"invalid score {j} encountered.skipping")
      continue
   else:
      print("Score:",j)


rows=int(input())
cols=int(input())
for i in range(rows):
    for j in range(cols):
        print("$",end="   ")
    print()


for i in range(0,30,4):
    print(i,end="  ")
    
       
    
