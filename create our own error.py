class WholeNumberError(Exception):
    pass
try:
    raise WholeNumberError("It's not a whole number")
except WholeNumberError as e:
    print(e)



x=int(input())
try:
    assert x>=0,"Not a Whole number"
except AssertionError as e:
    print(e)
else:
    print("Whole number")


#name error
try:
    print(age)#assign anything in age
except NameError as ne:
    print(ne)

#type error
try:
    s="Hello"
    a=s/2
except TypeError as b:
    print(b)

#Attribute error
try:
    s="Hello"
    print(s.uppercase())#use upper()
except AttributeError as ae:
    print(ae)
    
