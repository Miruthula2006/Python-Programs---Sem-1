#non-parameter
class Book:
    def __init__(self):
        self.name="harry potter"
        self.author="lowling"
    def show(self):
        print(f"{self.name}\n{self.author}")
b=Book()
b.show()
    
#parameter
class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
    def show(self):
        print(f"{self.name}\n{self.author}")
b=Book("harry potter","lowling")
b.show()

#default values
class Student:
    def __init__(self,name,age=12,classroom=7):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age,self.classroom)
Stu1=Student("Anu",12)
Stu1.show()
    
