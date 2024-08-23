""" 
EXCEPTION - Exception, also called as runtime error, is an abnormal condition in the code which occurs due to a logical mistake and can be handled. if not handled it would result in a different flow than the expected flow

ERROR - An error is an abnormal condition encountered in a code which leads to the termination of the code and needs to be fixed for the successful execution.

"""

""" Error """
print("hello")
# print('hello")  # Error


def add(a, b):
    return a + b


# print(add(23, 3, 45))  # add() takes 2 positional arg but 3 were given _ TypeError


""" Exception """


def div(a, b):
    return a / b


print(div(2, 3))  # 0.66666
# print(div(4, 0))  # ZeroDivisionError   _ work for all except 0 ( Exception )

arr = [1, 2, 3, 4]
print(arr[1])
print(arr[2])
# print(arr[4])       # Work well for all but len(arr)-1 except others ( Exception )
