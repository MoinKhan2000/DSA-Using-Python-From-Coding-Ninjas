"""             
    --> The __str__() method returns a human-readable, or informal, string representation of an object. This method is called by the built-in print(), str(),and format() functions.
    
    --> If you don't define a __str__() method for a class, then the built-in object implementation calls the __repr__() method instead.
    
"""


class Ocean:
    def __init__(self, seaCreatureName, seaCreatureAge):
        self.name = seaCreatureName
        self.age = seaCreatureAge


c = Ocean("Hii", 5)
# print(c)
# <__main__.Ocean object at 0x000001A3CA9EC4F0>

# print(str(c))
# <__main__.Ocean object at 0x000001A3CA9EC4F0>

# print(repr(c))
# <__main__.Ocean object at 0x000001A3CA9EC4F0>

# print(c.__str__())


class Ocean:
    def __init__(self, seaCreatureName, seaCreatureAge):
        self.name = seaCreatureName
        self.age = seaCreatureAge

    def __str__(self):
        return f"The creature type is {self.name} and the age is {self.age}"

    def __repr__(self):
        return f"Ocean('{self.name}', {self.age})"


c = Ocean("Hii", 5)
print(c)
# The creature type is Hii and the age is 5

print(str(c))
# The creature type is Hii and the age is 5

print(repr(c))
# Ocean('Hii', 5)
