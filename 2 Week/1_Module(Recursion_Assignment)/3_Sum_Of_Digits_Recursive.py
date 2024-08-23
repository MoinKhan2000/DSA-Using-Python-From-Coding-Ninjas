"""  
Sum of digits (recursive)
Send Feedback
Write a recursive function that returns the sum of the digits of a given integer.
Input format :
Integer N
Output format :
Sum of digits of N
Constraints :
0 <= N <= 10^9
Sample Input 1 :
12345
Sample Output 1 :
15
Sample Input 2 :
9
Sample Output 2 :
9

"""


def sumOfDigits(s):
    if len(s) == 0:
        return 0
    else:
        return int(s[0]) + int(sumOfDigits(s[1:]))


str = input()
print(sumOfDigits(str))
