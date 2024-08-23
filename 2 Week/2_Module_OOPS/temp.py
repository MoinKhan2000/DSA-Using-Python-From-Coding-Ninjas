"""

class Student:
    name="Rohan"
    age=16
s1=Student()
s2=Student()

print(s1.name,end="")
print(s2.name,end="")

"""

"""

class Student:
    name = "Parikh"

    def strore_details(self):
        self.age = 60

    def print_details(self):
        print(self.name, end=" ")
        print(self.age)


s = Student()
s.strore_details()
s.print_details()

"""

"""

class Student:
    name = "Parikh"

    def store_details(self):
        self.age = 60

    def print_details(self):
        print(self.age)


s = Student()
s.store_details()
s1 = Student()
s1.print_age()

"""

"""
class MyClass:
    pass


obj = MyClass()

print(obj.my_variable)  # This will output: None
"""


"""class student:
    def __init__(self, name, age):
        self.name = "Rohan"
        self.age = 20

    def print_details():
        print(self.name, end="")
        print(self.age)

s=student()
s.print_details()"""


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(self.name, end=" ")
        print(self.age)


s = student("Rohan", 60)
s.print_details()
