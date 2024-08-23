""" 
Try and except statements are used to catch and handle exceptions in Python.
Statements that can raise exceptions are kept inside the try clause and the statements that handle the exception are written inside except clause
"""

# a = [1, 2, 3]
# try:
#     print("second element", a[1])
#     print("third element = %d " % (a[2]))
#     print("fourth element", a[3])
# except:
#     print("exception occured")

# print("Executed successfully")


""" 
A try statement can have more than one except clause, to specify handlers for different exceptions. 
Please note that at most one handler will be executed. For example, we can add indexError in the previous code.
"""


def fun(a):
    if a < 5:
        # throws ZeroDivisionError for a=4
        b = a / a - 4
    # throws NameError if a>=5
    print("Value of b = ", b)


try:
    fun(3)
    print("hii")
    fun(5)  # Error occured here below line of code will not be executed from here.
    print("hii")
except ZeroDivisionError:
    print("ZeroDivisionError Occured and Handled")
except NameError:
    # this will be executed only when the exception is not handled by previous clauses
    #    raise Exception("Name Error occurred!")
    print("NameError Occured and Handled")
