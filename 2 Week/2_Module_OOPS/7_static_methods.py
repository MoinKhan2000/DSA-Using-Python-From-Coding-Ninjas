""" STATIC METHODS """
""" -->     Static methods are the methods that are bound to a class rather than its object. 
    -->     They do not require a class instance creation. So they are not dependent on the state of the object.
    -->     They can be called both by the class and its object.
    -->     Static methods are just like any other methods defined outside a class and just do some operations with some parameters passed.
    -->     The difference between the static methods and normal methods outside class is that the static methods logically make sense in the context of the class.
"""


class Calculoator:
    def subtract_number(n, m):
        return n - m

    @staticmethod
    def add_numbers(n, m):
        return n + m


# print(Calculoator.add_numbers(34, 3))
# print(Calculoator.subtract_number(34, 3))
class Product:
    count = 0

    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount
        self.id = Product.count
        Product.count += 1
        self.isAvailable = True if Product.count > 0 else False

    @staticmethod
    def calculateDiscount(price, discount):
        return price - price * discount

    def showProduct(self):
        availability = "Available" if self.isAvailable else "Not Available"
        discounted_price = self.calculateDiscount(self.price, self.discount)
        print(
            f"{self.id} {self.name}: ₹{self.price}/-, Discount: {self.discount}% Buy at the price of: ₹{discounted_price}/- only. Status : {availability}"
        )


print(Product.calculateDiscount(400, 0.5))

p1 = Product("LG-G8X", 70000, 0.12)
p1.showProduct()
