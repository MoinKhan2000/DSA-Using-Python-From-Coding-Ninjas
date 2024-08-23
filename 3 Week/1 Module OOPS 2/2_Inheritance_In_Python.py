""" Normal Way"""


class Product:
    def __init__(self, description):
        self.description = description

    def productDescription(self):
        print(self.description)


class LightProduct:
    max_weight_in_kg = 5

    def __init__(self, desc, weight):
        self.description = desc
        self.weight = weight

    def validateWeight(self):
        return self.weight <= self.max_weight_in_kg


pr = LightProduct("Hii it's 3 kg  weight which is less than 5", 3)
# print("Is valid:", pr.validateWeight())
# print(pr.description)


class VeryLightProduct(Product):
    pass


# vlp = VeryLightProduct("very light product")
# print(vlp.description)

# for el in dir(vlp):
#     print(el)


"""                     STANDARD WAY TO DO IT               """


class product:
    def __init__(self, desc):
        self.description = desc

    def productDescription(self):
        print(self.description)


class LightProduct(product):
    maxWeight = 5

    def __init__(self, desc, weight):
        self.weight = weight
        super().__init__(desc)

    def validateProduct(self):
        return self.weight <= LightProduct.maxWeight

    def printProduct(self):
        print(self.description, " and it's weight is", self.weight, "kg.")


# pr = LightProduct("mobile", 5)
# pr.productDescription()
# pr.printProduct()


"""         Constructor needs to be called it will never called its parent class constructor automatically          """


class A:
    def __init__(self):
        print("A constructor called! ")


class B:
    def __init__(self):
        print("B constructor called! ")


b = B()
