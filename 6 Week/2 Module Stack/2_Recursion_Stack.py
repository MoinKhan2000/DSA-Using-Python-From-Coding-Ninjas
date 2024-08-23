"""# Recursion Stack
Recursion is a technique of solving problems by breaking them down into smaller and simpler subproblems. The idea behind recursion is to solve the problem in terms
## 1. Introduction to recursion stack
### What is a recursive function?
A recursive function in Python is a function that calls itself during its execution. This allows the function to repeat a process indefinitely until a certain condition is met.

Here is an example of a recursive function in Python:


python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
​


In this example, the `factorial` function calculates the factorial of a given number `n`. The function calls itself with the argument `n-1` until it reaches the base case `n == 0`, at which point it returns the result of the factorial calculation.

"""

# Fact(5)->Fact(4)->Fact(3)->Fact(2)->Fact(1)->Fact(0) return
