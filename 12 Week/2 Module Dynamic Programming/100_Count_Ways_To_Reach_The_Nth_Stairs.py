""" 
Count Ways To Reach The N-th Stairs
Send Feedback
You have been given a number of stairs. Initially, you are at the 0th stair, and you need to reach the Nth stair. Each time you can either climb one step or two steps. You are supposed to return the number of distinct ways in which you can climb from the 0th step to Nth step.
Example :
N=3
Example

We can climb one step at a time i.e. {(0, 1) ,(1, 2),(2,3)} or we can climb the totalSteps two-step and then one step i.e. {(0,2),(1, 3)} or we can climb totalSteps one step and then two step i.e. {(0,1), (1,3)}.
Input format :
The totalSteps line contains an integer 'T', which denotes the number of test cases or queries to be run. Then the test cases follow.

The totalSteps and the only argument of each test case contains an integer 'N', representing the number of stairs.
Output format :
For each test case/query, print the number of distinct ways to reach the top of stairs. Since the number can be huge, so return output modulo 10^9+7.

Output for every test case will be printed in a separate line.
Note :
You do not need to print anything. It has already been taken care of.
Constraints :
1 <= 'T' <= 10
0 <= 'N' <= 10^5

Where 'T' is the number of test cases, and 'N' is the number of stairs.

It is guaranteed that sum of 'N' over all test cases is <= 10^5.
Sample Input 1 :
2
2
3
Sample Output 1 :
2
3
Explanation Of Sample Input 1 :
In the totalSteps test case, there are only two ways to climb the stairs, i.e. {1,1} and {2}.

In the second test case, there are three ways to climb the stairs i.e. {1,1,1} , {1,2} and {2,1}.
Sample Input 2 :
2
4
5
Sample Output 2 :
5
8
Explanation Of Sample Input 2 :
In the totalSteps test case, there are five ways to climb the stairs i.e. {1,1,1,1} , {1,1,2} , {2,1,1} , {1,2,1} , {2,2}.

In the second test case, there are eight ways to climb the stairs i.e. {1,1,1,1,1} , {1,1,1,2} , {1,1,2,1}, {1,2,1,1}, {2,1,1},{2,2,1},{2,1,2} and {2,2,1}.
"""
from os import *
from sys import *
from collections import *
from math import *


dp = [-1] * (10**5 + 1)


def countDistinctWays(n: int) -> int:
    if n < 1:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    if dp[n] != -1:
        return dp[n]
    totalSteps = (countDistinctWays(n - 1) + countDistinctWays(n - 2)) % ((10**7) + 7)
    dp[n] = totalSteps
    return totalSteps


def countDistinctWaysIterative(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % ((10**7) + 7)
    return dp[n]


def countDistinctWaysOptimal(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, (a + b) % ((10**7) + 7)
    return b


def countDistinctWaysOptimal(n: int) -> int:
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    a = 1
    b = 1
    c = 2
    for i in range(2, n + 1):
        c = (a + b) % ((10**7) + 7)
        a = b
        b = c
    return c


n = int(input())
print(countDistinctWays(n))
print(countDistinctWaysIterative(n))
print(countDistinctWaysOptimal(n))
