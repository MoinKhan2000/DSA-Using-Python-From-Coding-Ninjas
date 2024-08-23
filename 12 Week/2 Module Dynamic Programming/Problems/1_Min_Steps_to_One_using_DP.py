"""  
Min Steps to one using DP
Send Feedback
Given a positive integer 'n', find and return the minimum number of steps that 'n' has to take to get reduced to 1. You can perform any one of the following 3 steps:
1.) Subtract 1 from it. (n = n - ­1) ,
2.) If n is divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
3.) If n is divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ).  
Input format :
The first and the only line of input contains an integer value, 'n'.
Output format :
Print the minimum number of steps.
Constraints :
1 <= n <= 10 ^ 6
Time Limit: 1 sec
Sample Input 1 :
4
Sample Output 1 :
2 
Explanation of Sample Output 1 :
For n = 4
Step 1 :  n = 4 / 2  = 2
Step 2 : n = 2 / 2  =  1 
Sample Input 2 :
7
Sample Output 2 :
3
Explanation of Sample Output 2 :
For n = 7
Step 1 :  n = 7 ­- 1 = 6
Step 2 : n = 6  / 3 = 2 
Step 3 : n = 2 / 2 = 1  
"""
from sys import maxsize as MAX_VALUE
import sys


def countMinStepsToOne(n):
    dp = [-1] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        subtract_one = dp[i - 1]
        divide_by_two = MAX_VALUE if i % 2 != 0 else dp[i // 2]
        divide_by_three = MAX_VALUE if i % 3 != 0 else dp[i // 3]

        dp[i] = 1 + min(subtract_one, divide_by_two, divide_by_three)

    return dp[n]


n = int(input())
print(countMinStepsToOne(n))
