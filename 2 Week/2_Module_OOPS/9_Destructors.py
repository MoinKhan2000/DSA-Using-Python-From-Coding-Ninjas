"""                     DESTRUCTOR                      """
"""      -->    When an object is erased or destroyed in object-oriented programming, a destructer is invoked.
         -->    Before deleting an object, the destructor in python executes clean-up operations such as memory management.
         -->    Constructor is automatically called when an object is created, whereas destructor is called when an object is destroyed.
         -->    __del__() is referred to as destructor method. When all references to an object have been erased, i.e., once an object's garbage is collected, this method is invoked.
"""


class Computer:
    def __init__(self):
        print("Constructor Called !")

    def __del__(self):
        print("Destructor Called !")


def fun():
    c = Computer()
    return c


returnValue = fun()
print("hii")
print(returnValue)
