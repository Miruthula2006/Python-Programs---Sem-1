#Without arguments and without return type
def add():
    a=int(input())
    b=int(input())
    result=a+b
    print("Sum=",result)
add()

#Without arguments and with return type
def add():
    a=int(input())
    b=int(input())
    result=a+b
    return result
s=add()
print("Sum=",s)

#With arguments and with return type
def add(a,b):
    result=a+b
    return result
a=int(input())
b=int(input())
s=add(a,b)
print("Sum=",s)

#With arguments and without return type
def add(a,b):
    result=a+b
    print("Sum=",result)
a=int(input())
b=int(input())
add(a,b)
