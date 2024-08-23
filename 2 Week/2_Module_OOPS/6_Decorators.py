def square(n):
    return n * n


def cube(n):
    return n * n * n


s = square
sq = s
# print(square(3))  # 9
# print(s(4))  # 16
# print(sq(6))  # 36
# print(s, sq, square)
# <function square at 0x00000259CEE13E20> <function square at 0x00000259CEE13E20> <function square at 0x00000259CEE13E20>

"""             PASSING METHODS AS ARGUMENTS            """


def factors(fun, n):
    sq = fun(n)
    factors = []
    for i in range(2, sq):
        if sq % i == 0:
            factors.append(i)
    return factors


# print(factors(square, 10))
# print(factors(cube, 10))


"""         NESTED METHODS          """


def outer():
    def inner(name):
        return "Good Morning " + name

    return inner


# greet = outer()  # By calling outer function greet will take the inner function
# print(greet("Moin Khan"))  # Good Morning Moin Khan
# # As inner function is available here so calling inner function
# print(greet("Google"))  # Good Morning Google


def factorial(n):
    if n < 0:
        return "Provide a positive value"

    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)

    return fact(n)


# print(factorial(4))   # 24
# print(factorial(-10)) # Provide a positive value


"""         DECORATORS          """
"""             A Decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structre. Decorators are usually called before the definition of a function you to decorate               """


def upperCaseDecorator(fun):
    def toUpperCase(string):
        x = fun(string)
        x = x.upper()
        return x

    return toUpperCase


def greetNew(name):
    return "Hello " + name + " , How are you?"


upper = upperCaseDecorator(greetNew)
print(upper("Ali"))


def salaryUpdate(name):
    return "Congrats " + name + " !! Your Salary has been credited."


# print(salaryUpdate("kiran"))
# upper = upperCaseDecorator(salaryUpdate)
# print(upper("Kiran"))


def cube(fun):
    def inner(n):
        return fun(n) * n

    return inner


@cube  # Part of - Another way
def square(n):
    return n * n


# s = square
# c = cube(s)
# print(c(4))
# Another way to doing all these stuff


print(square(5))


"""             SCENARIO WHERE WE NEED TO USE DECORATOR FUNCTION            """
from datetime import datetime


def log_datetime(func):
    def wrapper():
        print(f'Function : {func.__name__}\nRun on : {datetime.today().strftime("%D")}')
        print(f'{"-"*30}')
        func()

    return wrapper


@log_datetime
def daily_backup():
    print("Daily data backup job has been finished")


daily_backup()
