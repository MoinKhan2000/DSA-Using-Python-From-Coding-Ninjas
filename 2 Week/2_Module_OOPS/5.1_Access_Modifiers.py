"""  
Access Modifiers    |    Public       |     Protected        |       Private
                    |                 |                      |  
Convention          |     var         |     _var             |      __var
                                                                    _class_var
"""


"""             PUBLIC          """


def printDict(dct):
    for el in dct:
        print(el, ":", dct[el])
    print()


def printList(dct):
    for el in dct:
        print(el)
    print()


class Product:
    count = 0

    def __init__(self, name, price, discount):
        self.id = Product.count + 1
        self.name = name  # public
        self._price = price  # private
        self.__discount = discount  # "__discount" is not accessed (protected)
        Product.count += 1


p1 = Product("Zen 24 inch TV", 10500, 500)
printDict(p1.__dict__)
p1.id = 23
printDict(p1.__dict__)
printList(dir(p1))


# One point which should be keep in mind
# print(p1.__discount)  # Cannot access since discount is private
print(p1._Product__discount)  # 500
# Using Classname then using __(Attribute) we can access it

p1._Product__discount = 1000
print(p1._Product__discount)  # 1000 ( We can even change the private member)

"""   

iN PYTHON, THE CONCEPT OF PRIVATE VARIABLES IS NOT STRICTLY ENFORCED - Instead, the convention of prefixing a variable with an underscore is used to indicate that the variable is intended to be private and should not directly accessed outside the class. This convention is just a hint to programmers, not a strict restriction enforced by the language, as in other programming languages like Java. The reason for this is to promote a philosophy of " we' are all consenting adults here" and to allow greater flexibility in the use of the language

"""
