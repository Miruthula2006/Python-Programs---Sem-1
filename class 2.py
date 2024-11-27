text="name is miruthula"
print("split=",text.split())#splits the string and returns a list
print("rsplit=",text.rsplit(","))#splits the string and returns a list(similar to split)

text="name is miruthula\n age is 17"
print("splitlines=",text.splitlines())#splits the string at line breaks and returns a list

text="my favourite car is"
x=text.rjust(30)#right aligns the string
print(x,"benz.")

text="benz"
x=text.ljust(20)#left align the string
print(x,"is my favourite car.")

text="i like cars and my fav cars are"
x=text.rfind("cars")#returns the last position of where it was found
y=text.rfind("r",5,10)
print(x)
print(y)

text="miruthula"
x="#".join(text)
print(x)
