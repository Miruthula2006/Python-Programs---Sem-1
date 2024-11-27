SMS={}
def add():
    Id=input()
    Name=input()
    Grade=input()
    Major=input()
    SMS["Id"]=Id
    SMS["Name"]=Name
    SMS["Grade"]=Grade
    SMS["Major"]=Major
    SMS[Id]={"Name":Name,"Grade":Grade,"Major":Major}
    print("Successfully added...")
def display():
    if len(SMS)!=0:
        print(SMS)
    else:
        print("Not found")
def remove():
    n=input()
    if n in SMS:
        del SMS[n]
        print("Student removed successfully...")
    else:
        print("Not found")
def update():
    n=input()
    if n in SMS:
        Grade=input()
        SMS.update({"Grade":Grade})
        print(SMS)
    else:
        print("Not found")
def search():
    n=input()
    if n in SMS:
        print(SMS[n])
    else:
        print("Not found")
def terminate():
    print("Goodbye")
    exit()
while True:
    print("1.Add\n2.Display\n3.Remove\n4.Update\n5.Search\n6.Exit")
    option=int(input())
    match option:
        case 1:
            add()
        case 2:
            display()
        case 3:
            remove()
        case 4:
            update()
        case 5:
            search()
        case 6:
            terminate()
        case _:
            print("ENTER A VALID OPTION")
            
            
            
