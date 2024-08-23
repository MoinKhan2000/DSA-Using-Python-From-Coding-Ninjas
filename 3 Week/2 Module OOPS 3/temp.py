"""try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Exception Occured")
"""

"""
try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Exception occured")
"""

"""
try:
    a = 10
    b = 0
    # print(d)
    c = a / b
except NameError:
    print("NameError occured")
except ZeroDivisionError:
    print("ZeroDivisionError Occured")
"""

"""
class ZeroDenominatorError(Exception):
    pass


try:
    a = 10
    b = 0
    if b == 0:
        raise ZeroDenominatorError()
    c = a / b
except ZeroDivisionError:
    print("Zero Division Error Occured")

# Zero Division Error Occured

"""
"""
# The above code defines a custom exception class called ZeroDenominatorError that inherits from the
# built-in ZeroDivisionError class, and raises this exception when a zero denominator is encountered
# in a division operation.

class ZeroDenominatorError(ZeroDivisionError):
    pass
try:
    a = 10
    b = 0
    if(b==0):
        raise ZeroDenominatorError()
    c = a/b
except ZeroDivisionError:
    print('Zero Division Error occured')
except ZeroDenominatorError:
    print('Zero Denominator Error occured')
    
"""

"""
class ZeroDenominatorError(ZeroDivisionError):
    pass
try:
    a = 10
    b = 0
    if b == 0:
        raise ZeroDenominatorError()
    c = a / b
except ZeroDivisionError:
    print("Zero Division Error occured ", end="")
except ZeroDenominatorError:
    print("Zero Denominator Error occured ", end="")
else:
    print("else works")
"""


class ZeroDenominatorError(ZeroDivisionError):
    pass


try:
    a = 10
    b = 5
    if b == 0:
        raise ZeroDenominatorError()
    c = a / b
except ZeroDivisionError:
    print("Zero Divisionb Error occured ", end="")
except ZeroDenominatorError:
    print("Zero Denominator Error occured ", end="")
else:
    print("else works")
