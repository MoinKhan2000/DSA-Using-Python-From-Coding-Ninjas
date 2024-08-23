"""     
    --> The members of a class that are declared protected are only accessible to a class derived from it
    --> Data members of a class are declared proteced by adding a single underscore _ symbol before the data member of that class.

"""


class Product:
    def __init__(self, desc):
        print("Parent class constructor called.")
        self._desc = desc
        self.__count = 1


class LightProduct(Product):
    """If there is no constructor in the child class parent class constructor calls automatically."""

    # def __init__(self, desc):
    #     print("Child class constructor called")

    def getDescription(self):
        return self._desc


p = LightProduct("Mobile Phone")
print(p.getDescription())
# print(p._desc)  # Although the _desc is protected but can be accessed using it's object
# print(p.__count)    # Here count is declared as private so we cannot access it anywhere
print(p._Product__count)
# Alternate idea for accessing the private member of the class    (Not REcommended)
