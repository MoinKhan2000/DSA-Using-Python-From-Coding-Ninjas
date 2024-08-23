"""class Vehicle:
    def __init__(self, color):
        self.color = color


class Car(Vehicle):
    def __init__(self, color, numGears):
        self.numGears = numGears


c = Car("black", 5)
print(c.color)

"""
"""

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(0, 0, 5, 10)
print(rect.area())
"""
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age);
        self.salary=salary
        
    def get_info(self):
        print('Name : ' + self.name)
        print('Age : '+ str(self.age))
        print('Salary : '+str(self.salary))

emp=Employee("Nancy",25,500000)
emp.get_info()

"""

"""
class Base:
    def __init__(self):
        self.__protected_var = 5


class Derived(Base):
    def __init__(self):
        Base.__init__(self)


class subDerived(Derived):
    def __init__(self):
        Derived.__init__(self)


obj = subDerived()
print(obj.__protected_var)
"""

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


person = Person("Prachi", 30)
print(person)
"""