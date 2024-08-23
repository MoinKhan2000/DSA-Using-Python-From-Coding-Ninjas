class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def printThePerson(self):
        print("Id of the Employee Is ", self.id)
        print("Name of the Employee Is :", self.name)


person1 = Person("Moin", 1)
person1.printThePerson()
person2 = Person("Moin", 1)
person2.printThePerson()
print(id(person1), id(person2))  # Different
print(person1 == person2)  # False
print(person1, person2)  # False
person1 = person2
print(id(person1), id(person2))  # Same
print(person1 == person2)  # True
print(person1, person2)  # Same

person1.printThePerson()  # Moin
person2.name = "Zara"  # Here person2 is pointing to p1 now if we change the value of person2 it will reflect in person1
person1.printThePerson()  # Zara
