'''
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Myfun(self):
        print("hello my name is " + self.name)
        


p1 = Person("abhi", 22)

p1.Myfun()
'''

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(self.fname, self.lname)

class Student(Person):
    pass

x = Student("abhi", "gaikwad")

x.print_name()

        
