class Animal:
    def speak(self):  # Ovverridden Method
        print("Animal speaking....")


class Dog(Animal):
    def speak(self):  # Overriding Method
        print("Woof.....")


class Cat(Animal):
    def speak(self):
        print("Meow.....")


c = Cat()
d = Dog()

# c.speak()
# Animal speaking....
# d.speak()
# Animal speaking....


# ##############################################################################
class Square:
    def drawSquare(self, length):
        print("Drawing a square of length", str(length))


class FilledSquare(Square):
    def drawSquare(self, length):
        # print("Drawing square of side :", length)  # Bad idea to do it
        super().drawSquare(length)  # Good way
        print("Filling the square....")


# square = FilledSquare()
# square.drawSquare(20)
# ##############################################################################
class Product:
    def __init__(self, description, price, discount):
        self.description = description
        self.price = price
        self.discount = discount

    def productDescription(self):
        return self.description

    def __calculateDiscount(self):
        return self.price - self.price * self.discount

    def getPrice(self):
        return self.__calculateDiscount()


class User:
    def __init__(self, customerType):
        self.customerType = customerType


class LightProduct(Product):
    maxWeight = 5

    def __init__(self, description, weight, price, discount):
        super().__init__(description, price, discount)
        self.weight = weight

    def validateWeight(self):
        return self.weight <= self.maxWeight

    def getPrice(self, user):
        if user.customerType == "premium":
            self.price = self.price - self.price * 0.15
        return super().getPrice()


user1 = User("standard")
user2 = User("premium")
product1 = LightProduct("Mobile LG-G8X", 2, 70000, 0.1)
product2 = LightProduct("Mobile LG-G8X", 2, 70000, 0.1)
print(product1.getPrice(user1))
print(product2.getPrice(user2))
