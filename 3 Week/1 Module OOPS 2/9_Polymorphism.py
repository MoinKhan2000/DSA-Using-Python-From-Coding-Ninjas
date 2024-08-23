""" 
POLYMORPHISM : The literal meaning of polymorphism is the condition of occurence in different forms.
"""
# Same len() function can operate on different collections.
# print(len("Moin Khan"))  # 9
# print(len([1, 2, 3, 4, 5, 6, 7]))  # 7
# print(len([[1, 2, 3, 4, 4], ["Moin", {"Moin", "Khan"}, "Moile", "Computer"]]))  # 2


def add(x, y, *z):
    return x + y + sum(z)


# print(add(2, 3, 3))  # 8
# print(add(2, 3, 1, 2, 3))  # 11
# print(add(2, 3))  # 5

# ###################################################################################################################


class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is developed country.")


obj_ind = India()
obj_usa = USA()


# for country in (obj_ind, obj_usa):    # here it became touple
#     country.capital()
#     country.language()
#     country.type()

# ###################################################################################################################


class Animal:
    def speak(self):
        return "Which Animal?"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

# ###################################################################################################################


class India:
    def capital(self):
        print("New Delhi is the capital of India")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA")


def func(obj):
    obj.capital()


obj_ind = India()
obj_usa = USA()

func(obj_usa)
func(obj_ind)
