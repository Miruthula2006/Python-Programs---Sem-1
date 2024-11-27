d={"Name":"Miruthula","Age":17,"Degree":["B.Sc","AI"],"LastName":"Murugan"}#to store multiple values in a key(list)
print(d)#creating a dictionary
print(d["Name"])#1 to display a specific value
print(d.get("Degree"))#2 to display a specific value
d["Age"]=18#to change a particular key value
print(d)

k=d.keys()#returns the keys of dictionary
print(k)
v=d.values()#returns the values of dictionary
print(v)
kv=d.items()#returns the key value pairs of dictionary
print(kv)

d.update({"Age":17})#updates the already available data
print(d)
d["Gender"]="Female"#to add new key-value pair
print(d)

d.pop("LastName")#removes the mentioned key from the dictionary
print(d)
d.popitem()#removes the last inserted item
print(d)
del d["Degree"]
print(d)

                   #TO DISPLAY KEYS IN NEW LINES(2 WAYS)
for i in d:
    print(i)

for i in d.keys():
    print(i)
                   #TO DISPLAY VALUES IN NEW LINES(2 WAYS)
for i in d:
    print(d[i])

for i in d.values():
    print(i)
                   #TO COPY A DICTIONARY FROM ANOTHER(2 WAYS)
d2=d.copy()
print(d2)

d2=dict(d)
print(d2)






