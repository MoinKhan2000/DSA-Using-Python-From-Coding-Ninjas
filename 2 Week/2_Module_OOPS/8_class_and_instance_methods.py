"""         CLASS METHODS               """
""" --> Class methods are created using the @classmethod decorator and like static methods they don't need an instance to be invoked. 
    --> Class methods know about their class. They can't access specific instance data, but they can call other static methods.
    --> Class methods don't need self as an argument, but they do need a parameter called cls. This stands for class, and like self, gets automatically passed in by python.
    --> Instance methods are the most common type of methods in Python classes.
    --> These are so called because they can access unique data of their instance.
    --> Instance methods must have self as a parameter, but you don't need to pass this in every time. Python does that for you.
    --> They are used to read, modify instance level attributes and also perform operations on at instance level.

"""


class Employee:
    __company = "YaHu Solutions"

    def __init__(self, id, name, salary):
        self.__id = id
        self.__name = name
        self.__salary = salary

    @staticmethod
    def greet():
        return "Have a great day"

    @classmethod
    def intro(cls):
        return "Welcome To " + cls.__company + ". " + cls.greet()


# print(Employee.intro())
# print(Employee.greet());


class Product:
    __count = 0

    def __init__(self, name, price, discount):
        self.__id = self.__count + 1
        self.__name = name
        self.__price = price
        self.__discount = discount
        self.__isAvailable = True
        Product.__count += 1

    @staticmethod
    def checkOwner(product):
        return product.getName().startswith("CN_")

    @classmethod
    def totalProducts(cls):
        return cls.__count

    # Instance Methods

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price - self.__price * self.__discount

    def getId(self):
        return self.__id


class Cart:
    __max_capacity = 20
    __count = 0

    def __init__(self, user):
        self.__id = self.__count + 1
        self.__user = user
        self.__items = {}
        Cart.__max_capacity += 1

    @staticmethod
    def getCoupenCodes():
        return ["MOIN_2023", "NEW_YEAR_2023", "EID_2023"]

    @classmethod
    def updateMaxCapacity(cls, newCapacity):
        cls.__max_capacity = newCapacity

    def addItem(self, product):
        self.__items.update({product.getId(): product})

    def getItems(self):
        return self.__items

    def generateBill(self):
        print("hii")
        total = 0
        for el in self.__items.values():
            print(el)
            total = total + el.getPrice()
        return total


c1 = Cart("Moin Khan")
p1 = Product("CN_cn_asdf", 4000, 0.1)
p2 = Product("Car", 5400000, 00)
c1.addItem(p2)
c1.addItem(p1)
print(c1.generateBill())
print(c1.getItems())

"""                 CODE WITH HARRY                 """


# we use class methods these are useful when you have to do any changes in the class
class Employee:
    company = "Apple"

    def show(self):
        print("Company Name:", self.company)

    @classmethod  # without this Employee.company will not be changed (class variables )
    def changeCompany(cls, newCompany):
        cls.company = newCompany


# ep = Employee()
# ep.company = "Tesla"
# ep.show()
# ep.changeCompany("Tesla")
# print(Employee.company)  # Apple


"""                 SUMMARY                 """
""" 
1. Static Methods : Cannot accesss anything else in the class. Totally self contained code.
2. Class Methods : Can access limited methods in the class. Can modify class specific details.
3. Instance Methods : The most common method type. Able to access data and properties unique to each instance.
"""
