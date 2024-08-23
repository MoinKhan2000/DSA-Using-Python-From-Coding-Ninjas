class Product:
    company = "SC"

    def __init__(self, id, company):
        self.id = id
        self.company = company


p = Product(1, "ABC")
print(p.company)
p2 = Product
print(p2.company)


class Student:
    def __init__(self):
        print("Student self ", self)
        # Self is nothing but the reference of the object
        #  <__main__.Student object at 0x00000284D402F1F0>


s1 = Student()
print(s1)
#  <__main__.Student object at 0x00000284D402F1F0>
