"""  
Subset Sum Equal To K
Send Feedback
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.
Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.
For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.
Input Format :
The first line contains a single integer T representing the number of test cases.

The first line of each test case contains two space-separated integers ‘N’ and ‘K’ representing the size of the input ‘ARR’ and the required sum as discussed above.

The next line of each test case contains ‘N’ single space-separated integers that represent the elements of the ‘ARR’.
Output Format :
For each test case, return true or false as discussed above.
Output for each test case will be printed in a separate line.
Note:
You don’t need to print anything, it has already been taken care of. Just implement the given function.
Constraints:
1 <= T <= 5
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
0 <= K <= 10^3

Time Limit: 1 sec
Sample Input 1:
2
4 5
4 3 2 1
5 4
2 5 1 6 7
Sample Output 1:
true
false
Explanation For Sample Input 1:
In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
Sample Input 2:
2
4 4
6 1 2 1
5 6
1 7 2 9 10
Sample Output 2:
true
false
Explanation For Sample Input 2:
In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.
"""
from os import *
from sys import *
from collections import *
from math import *


def subsetSumUtil(ind, target, arr, dp):
    if target == 0:
        return True
    elif ind == 0:
        return True if arr[0] == target else False
    if dp[ind][target] != -1:
        return dp[ind][target]
    notTakeIt = subsetSumUtil(ind - 1, target, arr, dp)
    takeIt = False
    if target >= arr[ind]:
        takeIt = subsetSumUtil(ind - 1, target - arr[ind], arr, dp)
    dp[ind][target] = takeIt or notTakeIt
    return dp[ind][target]


def subsetSumToK(n, k, arr):
    # Initialize a memoization table with -1.
    dp = [[-1 for j in range(k + 1)] for i in range(n)]

    # Call the utility function to find if a subset with the given target sum exists.
    return subsetSumUtil(n - 1, k, arr, dp)
