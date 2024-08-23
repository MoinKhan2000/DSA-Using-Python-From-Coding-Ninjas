"""
SINGLE IINHERITANCE - Single inheritance is when a class inherits from only one parent class
        class A:
        class B(A):
"""

""" 
Let's say we have a vehicle class that has a start_engine method. We can create a Car class that inherits from vehicle and adds new properties and method specific to cars, such as accelerate and brake
"""


class Vehicle:
    def start_engine(self):
        print("Starting Engine.....")


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__()
        self.make = make
        self.model = model
        self.year = year

    def accelerate_car(self):
        print("Accelerating......")

    def brake(self):
        print("Braking....")

    def showCar(self):
        return f"Make : {self.make}, \nModel : {self.model}, \nYear: {self.year}"


# c = Car("RRR", "l-31", 2029)
# c.start_engine()
# c.accelerate_car()
# c.brake()


"""
MULTIPLE INHERITANCE - Multiple inheritance is when a class inherits from two or more parent classes.
class A:
class B:
class C(A,B)

Let's say we are building a SmartPhone class that needs to inherit from Phone and Computer classes. The Phone class provides functionalities such as making calls and sending messages, while the Computer class provides functionalities such as browsing the internet and sending emails.
  
"""


class Phone:
    def makeCall(self):
        print("Making call....")

    def sendMsg(self):
        print("Sending message....")


class Computer:
    def browseInternet(self):
        print("Browsing internet....")

    def sendEmail(self):
        print("Sending email.....")


class SmartPhone(Phone, Computer):
    def __init__(self, model, year) -> None:
        # super().__init__()
        self.model = model
        self.year = year

    def showPhone(self):
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")

    def showAllActivities(self):
        print("-" * 30)
        self.makeCall()
        self.sendMsg()
        self.browseInternet()
        self.sendEmail()
        print("-" * 30)


# smart = SmartPhone("Lg-G8X", 2019)
# smart.showPhone()
# smart.showAllActivities()


"""
MULTILEVEL INHERITANCE - Multilevel inheritance is when a class inherits from a parent class, which in turn inherits from another parent class.
class A:
class B(A):
class C(B)

Let's say we have a User class that has a name and email attributes. We can create a Customer class that inherits from User and adds a cart attribute. We can then create a Premium Customer class that inherits from Customer and adds a discount attribute.
  
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Customer(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.cart = []

    def buyItem(self, item):
        self.cart.append(item)


class PremiumCustomer(Customer):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.discount = 0.1

    def applyDiscount(self, price):
        return price * (1 - self.discount)
