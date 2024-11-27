def display():
    if n==0:
        print("No Books Available")
    else:
        print(L)
def add():
    L.append(input())
    print(L)
def remove():
    r=input()
    if r in L:
         L.remove(r)
         print(L)
    else:
        print(f"{r} not in the Library")
n=int(input())
L=[]
for i in range(n):
    L.append(input())
display()
add()
remove()

def display():
    print(Inventory)
def add():
    Inventory.update({"Chocolate":150})
    print(Inventory)
def remove():
    Inventory.pop("Tomato")
    print(Inventory)
Inventory={"Tomato":50,"Soap":40,"Oil":100}
display()
add()
remove()





    

