class Product:
    def __init__(self, price) -> None:
        # self.price = price  # Public    - Accessible
        # self.__price = price    # Private - throw an error ElectricProduct obj has no attr 'price' but if we really want to get the private member in the child class we can access it using _Product__price
        # self._price = price  # Protected - Accessible

        self.__price = price

    def returnPrivatePrice(self):
        return self.__price


class ElectricProduct(Product):
    def __init__(self, desc, price):
        self.desc = desc
        super().__init__(price)

    def getPrice(self):
        # return self.price
        # return self.__price
        # return self._price  # throgh an error since price is no longer protected it became private.
        return self.returnPrivatePrice()

    def getDescription(self):
        return self.desc


p = ElectricProduct("Lg - g8x mobile", 1000)
# print(p.getDescription(), "and it's price is", p.getPrice())

# print(dir(p))
"""         
[
 '_Product__price',     # here price is private
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_price',      # here _price is protected
 'desc',
 'getDescription',
 'getPrice'
 ]
"""


# #################################################### ##########################################


class Product:
    def __init__(self, desc, price, dis):
        self.desc = desc
        self.price = price
        self.discount = dis

    def productDescription(self):
        print(self.desc)

    # Private function
    def __calculateDiscount(self):
        return self.price - self.price * self.discount

    # Accessing private function in the same class - Accessible
    def getPrice(self):
        return self.__calculateDiscount()


class LightProduct(Product):
    maxWeight = 5

    def __init__(self, desc, weight, price, disc):
        self.weight = weight
        super().__init__(desc, price, disc)

    def validateWeight(self):
        return self.weight <= self.maxWeight

    def getPrice(self):  # Method overriding
        self.price = self.price - self.price * 0.15
        # Giving extra 15% discount on each product of LightProduct clsss
        return super().getPrice()

    def showProduct(self):
        print("*" * 40)
        print(
            "Description Of The Product :",
            self.desc,
            "\n" "Weight Of The Product :",
            str(round((float)(self.weight), 2)),
            "\n" "Price Of The Product : ",
            (self.getPrice()),
        )
        print("*" * 40)


p = LightProduct("Speacker SONY", 3, 4000, 0.1)
# print(p.getPrice())
p.showProduct()
