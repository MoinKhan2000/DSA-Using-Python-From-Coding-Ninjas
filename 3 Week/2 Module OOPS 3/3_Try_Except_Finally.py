"""
def calculate_bmi(h, w):
    '''Calculate body mass index (BMI)'''
    return w / h**2

def main():
    try:
        h = float(input("Height  - "))
        w = float(input("Weight - "))
    except ValueError as e:
        print("Error ! Please enter a valid number.")
    else:
        bmi = round(calculate_bmi(h, w))
        evaluation = evaluate_bmi(bmi)

        print(f"Your body mass index is {bmi}")
        print(f"This is considered {evaluation}")

def evaluate_bmi(bmi):
    '''Evaluate BMI'''
    if 18.5 <= bmi <= 24.9:
        return "healty"
    elif bmi >= 25:
        return "overweight"
    else:
        return "underweight"
main()
"""


"""
Whenever a current method terminates abruptly, there are chances that the method may have been using resources that are allocated to it and will not be freed or closed upon the termination of the current method. 

In such situations finally, a block of code is used to free the resources that were allocated in the try block of code and this finally block of code is always executed regardless of the exception being handled by the except block or not.

"""


def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero")
    else:
        print("Your answer is ", result)
    finally:
        print("This is always executed")


divide(3, 2)
print()
divide(3, 0)
