class first:
    pass


f1 = first()
print(f1.__dir__)
print(f1)

f2 = first()
print(f2.__dir__)
print(f2)

"""
<built-in method __dir__ of first object at 0x0000022201DCC460>
<__main__.first object at 0x0000022201DCC460>
<built-in method __dir__ of first object at 0x0000022201DCC2B0>
<__main__.first object at 0x0000022201DCC2B0>
"""


# class Product:
#     id = 0
#     name = "headphones"

#     def __init__(self):
#         self.id = Product.id + 1


# p1 = Product
# print(p1.name)
# print(p1.__dict__)

# p2 = Product
# print(p2.name)
# print(p1.id)  # 0
# print(p2.id)  # 0


class Items:
    count = 0

    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount
        self.id = Items.count + 1
        Items.count += 1
        print(
            f"Item {self.id}. {name} cost : {price}rupee  and discount : {discount}rupee  purchase at the rupee of {price-discount}/- only. "
        )


item1 = Items("Television", 15000, 1500)
item2 = Items("Lg-g8x", 69000, 11000)
item3 = Items("Sony Home Theater 3x10", 3500, 1015)
