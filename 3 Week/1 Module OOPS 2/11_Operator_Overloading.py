# print(2 + 3)
# 5
# print([1, 2, 3] + [4, 5, 6])
# [1, 2, 3, 4, 5, 6]
# print("Moin " + "Khan")
# Moin Khan
# print([[1, 2, 3], ["a", "b", "c"]] + [[10, 20, 30], ["x", "y", "z"]])
# [[1, 2, 3], ['a', 'b', 'c'], [10, 20, 30], ['x', 'y', 'z']]
# print(2 * 3)
# 6
# print([1, 2, 3] * 3)
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print("_" * 30)
# ______________________________


"""
OPERATOR OVERLOADING : Operator overloading means giving extended meaning beyond their predefined operational meaning.
"""


class Number:
    def __init__(self, number):
        self.number = number

    # Override the __add__ ,__mul__, __sub__ methods, to get the add, multiply, subtraction functionalities.
    def __add__(self, other):
        return self.number + other.number

    def __mul__(self, other):
        return self.number * other.number

    def __sub__(self, other):
        return self.number - other.number


a = Number(2)
b = Number(3)
"""
print(a + b)  # 5
print(a * b)  # 6
print(a - b)  # -1
"""


# *****************************************************************************************************
class Square:
    def __init__(self, side):
        self.side = side

    def drawSquare(self):
        print("Drawing a square of", self.side, "and area", (self.side**2))

    def __add__(self, other):
        return Square(self.side + other.side)


sq1 = Square(4)
sq1.drawSquare()


sq2 = Square(5)
sq2.drawSquare()

sq3 = sq1 + sq2
sq3.drawSquare()
