""" 
Triangle
Send Feedback
You are given a triangular array/list 'TRIANGLE'. Your task is to return the minimum path sum to reach from the top to the bottom row.
The triangle array will have N rows and the i-th row, where 0 <= i < N will have i + 1 elements.
You can move only to the adjacent number of row below each step. For example, if you are at index j in row i, then you can move to i or i + 1 index in row j + 1 in each step.
For Example :
If the array given is 'TRIANGLE' = [[1], [2,3], [3,6,7], [8,9,6,1]] the triangle array will look like:

1
2,3
3,6,7
8,9,6,10

For the given triangle array the minimum sum path would be 1->2->3->8. Hence the answer would be 14.
Input Format :
The first line of input contains an integer ‘T’ denoting the number of test cases to run. Then the test case follows.

The first line of each test case contains an integer ‘N’  representing the length of the array/list triangle.

Then N lines follow. Each of the ith row contains i + 1 space-separated integers denoting the elements of the array/list 'TRIANGLE'.
Output Format :
For each test case, print an integer X representing the minimum path sum.

Output for each test case will be printed in a separate line.
Note :
You don’t need to take input or print anything, it already has been taken care of. Just implement the function.
Constraints :
1 <= T <= 5
1 <= N <= 10^3 
-10^6 <= TRIANGLE[i][pos] <= 10^6 ,                

Where 'TRIANGLE[i][pos]' is the element at row = 'i' & position = 'pos' in triangle array.  

Time limit: 1 sec
Sample Input 1 :
2
4
2 
3 4
6 5 7
4 1 8 3
1
-10 
Sample output 1 :
11
-10
Sample Input explanation:
Test case 1:
Here our triangle array is:

2
3 4
6 5 7 
4 1 8 3

In this array, the minimum path will be 2->3->5->1, so the minimum sum path would be 2+3+5+1=11

Test case 2:
In this case, there is one row. Thus, the minimum path will be -10, and the minimum sum path=-10.
Sample input 2 :
2
4
1
2 3
4 5 6
7 8 9 10
3
5
-1 3
22 1 -9
Sample Output 2 :
14
-1
"""

from os import *
from sys import *
from collections import *
from math import *


def f(i, j, triangle, n, dp):
    if i == n - 1:
        return triangle[n - 1][j]
    if dp[i][j] != -1:
        return dp[i][j]
    down = triangle[i][j] + f(i + 1, j, triangle, n, dp)
    diag = triangle[i][j] + f(i + 1, j + 1, triangle, n, dp)
    dp[i][j] = min(down, diag)
    return dp[i][j]


def minimumPathSumRecursive(triangle, n):
    dp = [[-1 for j in range(n)] for i in range(n)]
    return f(0, 0, triangle, n, dp)


def minimumPathSumIterative(triangle, n):
    dp = [[-1 for j in range(n)] for i in range(n)]
    for j in range(0, n):
        dp[n - 1][j] = triangle[n - 1][j]

    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            down = triangle[i][j] + dp[i + 1][j]
            diag = triangle[i][j] + dp[i + 1][j + 1]
            dp[i][j] = min(down, diag)
    return dp[0][0]


def minimumPathSumOptimal(triangle, n):
    first = [-1 for i in range(n)]
    for j in range(n):
        # making a first list of size j
        first[j] = triangle[n - 1][j]

    for i in range(n - 2, -1, -1):
        second = [-1 for j in range(i + 1)]
        for j in range(i, -1, -1):
            down = triangle[i][j] + first[j]
            diag = triangle[i][j] + first[j + 1]
            second[j] = min(down, diag)
        first = second[:]
    return first[0]


def main():
    # Define the input triangle and its size
    triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
    n = len(triangle)

    # Call the minimumPathSum function and print the result
    print(minimumPathSumRecursive(triangle, n))
    print(minimumPathSumIterative(triangle, n))
    print(minimumPathSumOptimal(triangle, n))


if __name__ == "__main__":
    main()
