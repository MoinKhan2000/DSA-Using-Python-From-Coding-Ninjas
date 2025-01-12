""" 
Shortest Common Supersequence
Send Feedback
Given two strings, ‘A’ and ‘B’. Return the shortest supersequence string ‘S’, containing both ‘A’ and ‘B’ as its subsequences. If there are multiple answers, return any of them.
Note: A string 's' is a subsequence of string 't' if deleting some number of characters from 't' (possibly 0) results in the string 's'.
For example:
Suppose ‘A’ = “brute”, and ‘B’ = “groot”

The shortest supersequence will be “bgruoote”. As shown below, it contains both ‘A’ and ‘B’ as subsequences.

A   A A     A A
b g r u o o t e
  B B   B B B  

It can be proved that the length of supersequence for this input cannot be less than 8. So the output will be bgruoote.
Input Format:
The first line of the input contains a single integer ‘T’ representing the no. of test cases.

The first line of each test case contains a single string ‘A’, denoting the first string described in the problem.

The second line of each test case contains a single string, ‘B’, denoting the second string described in the problem.
Output Format:
For each test case, print the shortest string ‘S’, which contains ‘A’ and ‘B’ as its subsequences.

Print a separate line for each test case.
Note:
You are not required to print anything; it has already been taken care of. Just implement the function and return the answer.
Constraints:
1 ≤ T ≤ 100
1 ≤ |A|, |B| ≤ 1000
Both strings consist of only lowercase English letters.
1 ≤ Σ(|A|+|B|) ≤ 3000

Time limit: 1 Sec
Sample Input 1 :
2
brute
groot
bleed
blue
Sample Output 1 :
bgruoote
bleued
Explanation For Sample Input 1 :
For First Case - Same as explained in above example.

For the second case - 

‘A’ = “bleed”, and ‘B’ = “blue”

The shortest supersequence will be “bleued”. As shown below, it contains both ‘A’ and ‘B’ as subsequences.

A A A   A A
b l e u e d
B B   B B

It can be proved that the length of supersequence for this input cannot be less than 6. So the output will be bleued.
Sample Input 2 :
2
coding
ninjas
blinding
lights
Sample Output 2 :
codningjas
blindinghts

"""
from os import *
from sys import *
from collections import *
from math import *


def lcsIter(s, t):
    n = len(s)
    m = len(t)
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    for j in range(0, m + 1):
        dp[0][j] = 0

    for i in range(0, n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    string = ""

    i = n
    j = m
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            string += s[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            string += s[i - 1]
            i -= 1
        else:
            string += t[j - 1]
            j -= 1
    while i > 0:
        string += s[i - 1]
        i -= 1
    while j > 0:
        string += t[j - 1]
        j -= 1
    return string[::-1]


def shortestSupersequence(a: str, b: str) -> str:
    return lcsIter(a, b)
