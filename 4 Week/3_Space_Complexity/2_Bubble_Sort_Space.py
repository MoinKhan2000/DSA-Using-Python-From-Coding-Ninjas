# Bubble Sort
""" 
basically bubble sort function takes an array 
initialize i=0
and compare i with i+1 for multiple elements 
here we are not making duplicate array although we are required number of constant varibales to compare but it's in the constant amount 
Means O(1)
"""

""" 
Factorial iterative
Here factorialIterative(n) takes an input 
here we found fact of n*n-1*n-2 using iterative approach
i=1
for i=1 i<n: 
    fact*=i;
using this approach we are constantly using the same variable means O(1)

"""

""" 
Factorial - Recursive
factorialRecursive(n):
if (n==1 or n ==0 )
return 1 ;
else return n * factorialRecursive(n-1);

fact(n)->fact(n-1)->fact(n-2)->fact(n-3)---------1
fact(4)->fact(5)->fact(6)->fact(7)--------->1

here n waits for n-1 to solve and n-1 waits for n-2 to resolve n-2 waits for n-3 to resolve all these calls are not distroy until the base condition is met. 
 
so O(n)

"""


def multiplyRec(m, n):
    if n == 1:
        return m
    return m + multiplyRec(m, n - 1)


print(multiplyRec(4, 5))  
