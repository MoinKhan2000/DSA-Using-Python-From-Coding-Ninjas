"""

MULTIPLE INHERITENCE

class Vehicle:
     def __init__(self,color):
         self.__color = color
class Car(Vehicle):
    def __init__(self,color,numGears):
        super().__init__(color)
        self.numGears = numGears
    def printCar(self):
        print(c.__color,end=" ")
        print(c.numGears)
c = Car("black",5)
c.printCar()
"""

"""
class A:
    def __init__(self):
        self.a = 10

    def method_A(self):
        print("This is method A of class A")


class B(A):
    def __init__(self):
        super().__init__()
        self.b = 20

    def method_B(self):
        print("This is method B of class B")


class C:
    def __init__(self):
        self.c = 30

    def method_C(self):
        print("This is method C of class C")


class D(B, C):
    def __init__(self):
        super().__init__()
        self.d = 40

    def method_D(self):
        print("This is method D of class D")
"""

"""
class Vehicle:
    def __init__(self, color):
        self.color = color


class Car(Vehicle):
    def __init__(self, color, numGears):
        super().__init__(color)
        self.numGears = numGears


c = Car("BLACK", 5)
print(c.color)
"""
"""

class A:
    def __init__(self):
        print('init of A called')

class B:
    def __init__(self):
        print('init of B called')
        
class C(B,A):
    def __init__(self):
        super().__init__();
        
c=C();
"""

"""
class X: 
      pass
class Y: 
      pass
class Z:
      pass
class A(X,Y):
      pass
class B(Y,Z):
      pass
class C(B,A,Y):
      pass


print(C.mro())

# print(C>B>A>X>Y>Z)
"""
"""

class Vehicle:
    def __init__(self, color):
        self.color = color

    def print(self):
        print(c.color, end="")


class Car(Vehicle):
    def __init__(self, color, numGears):
        super().__init__(color)
        self.numGears = numGears

    def print(self):
        self.print();
        print(c.numGears)


c = Car("black", 5)
c.print()
"""
"""
class Animal:
    def sound(self):
        print('An animal makes a sound')

class Dog(Animal):
    def sound(self):
        super().sound() 
        print('A dog barks')

a=Animal();
d=Dog()
a.sound();
d.sound();
"""


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())
