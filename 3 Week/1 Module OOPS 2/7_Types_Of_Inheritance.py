"""
HIERARCHICHAL INHERITANCE - Hierarchichal inheritance is when multiple subclasses inherits from the same base class
class A:
class B(A):
class C(A):
class D(A):

Let's say we have a Shape class that has a calculateArea method. We can create multiple subClasses that inherit from Shape, such as Rectangle, Circle, and Triangle.
  
"""


class Shape:
    def calculateArea(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculateArea(self):
        return (0.5) * self.base * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return 3.14 * self.radius**2


"""
HYBRID INHERITANCE - Hybrid inheritance is a combination of multiple and multilvel inheritance. It is when a class inherits from multiple classes and also inherits from a subclass.
class A:
class B(A):
class C(A):
class D(B,C)

Let's say we have a BankAccount class that has a balance attribute and methods for depositing and withdrawing money.

We can create a SavingAccount class that inherits from BankAccount and adds a interestRate attribute and a method for calculating interest.

We can then create a CreditCard class that also inherits from BankAccount and adds a creditLimitAttribute and methods for making purchases and payments.

Finally, we can create a StudentAccount class that inherits from both SavingAccount and CreditCard classes and adds a studentDiscountAttribute

                         |--- CreditCard   ---- |
        BankAccount -----                        ------ StudentAccount
                         |--- SavingAccount---- |

"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Balance...")


class SavingAccount(BankAccount):
    def __init__(self, balance, interestRate):
        super().__init__(balance)
        self.interest_rate = interestRate

    def calculateInterest(self):
        if self.interest_rate >= 1:
            return self.balance * self.interest_rate


class CreditCard(BankAccount):
    def __init__(self, balance, creditLimit):
        super().__init__(balance)
        self.creditLimit = creditLimit

    def makePurchase(self, amount):
        if self.balance + self.creditLimit >= amount:
            self.balance -= amount
        else:
            print("Credit Limit exceeded.")


class StudentAccount(SavingAccount, CreditCard):
    def __init__(self, balance, interestRate, creditLimit, studentDiscount):
        SavingAccount.__init__(self, balance, interestRate)
        CreditCard.__init__(self, balance, creditLimit)
        self.studentDiscount = studentDiscount

    def applyDiscount(self, price):
        return price * (1 - self.studentDiscount)
