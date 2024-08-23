""" 
Using raise Keyword
        -->Python raise keyword is used to raise exceptions or errors. The raise keyword raises an error and stops the control flow of the program. It is used to bring up the current exception in an exception handler so that it can be handled further up the call stack
"""

# a = 5
# if a % 2 != 0:
#     raise Exception("The number should not be an odd integer")

# s = "apple"
# try:
#     num = int(s)
# except ValueError:
#     raise ValueError("String cannot be changed into an error")


# s = "apple"
# try:
#     num = int(s)
# except:
#     raise
# ValueError: invalid literal for int() with base 10: 'apple'


"""
 Using Exceptions Class
    --> In python we can define custom exceptions by creating a new class that is derived from the built-in Exception class.
"""


class InvalidAgeException(Exception):
    "Raised when the input is less than 0"
    pass


number = 18

try:
    num = int(input("Enter your age : "))
    if num <= 0:
        raise InvalidAgeException
    else:
        print("Welcome User")
except:
    print("Exception Occured : Invalid Age")


class SalaryNotInRangeError(Exception):
    def __init__(self, salary, msg="Salary is not in (500,15000) range"):
        self.salary = salary
        self.message = msg
        super().__init__(self.message)


salary = int(input("Enter salary amount : "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
    # alaryNotInRangeError: Salary is not in (500,15000) range for input 1000
