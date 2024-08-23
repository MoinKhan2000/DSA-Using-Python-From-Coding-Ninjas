""" 
Number Of Subsets
Send Feedback
You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.


Find the number of ways of selecting the elements from the array such that the sum of chosen elements is equal to the target 'k'.


Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.


Example:
Input: 'arr' = [1, 1, 4, 5]

Output: 3

Explanation: The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.
Input Format :
The first line contains two space-separated integers ‘n’ and 'k', denoting the size of the array and the target sum.

The second line contains ‘n’ space-separated integers denoting the elements of the array.


Output Format :
Print the number of ways we can choose elements from 'arr' such that their sum is equal to 'k'.


Note :
You do not need to print anything, it has already been taken care of. Just implement the given function.
Sample Input 1 :
4 5
1 4 4 5


Sample Output 1 :
 3


Explanation For Sample Output 1:
The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.


Sample Input 2 :
3 2
1 1 1


Sample Output 2 :
3


Explanation For Sample Output 1:
There are three 1 present in the array. Answer is the number of ways to choose any two of them.


Sample Input 3 :
3 40
2 34 5


Sample Output 3 :
0


Expected time complexity :
The expected time complexity is O('n' * 'k').


Constraints:
1 <= 'n' <= 100
0 <= 'arr[i]' <= 1000
1 <= 'k' <= 1000

Time limit: 1 sec
"""
from typing import List


def f(ind, sum, arr, dp):
    if sum < 0:
        return 0

    if ind == len(arr):
        if sum == 0:
            return 1
        return 0

    if dp[ind][sum] != -1:
        return dp[ind][sum]

    # If we take the ith element.
    Take = f(ind + 1, sum - arr[ind], arr, dp)
    # If we do not take the ith element.
    Take = Take + f(ind + 1, sum, arr, dp)

    dp[ind][sum] = Take
    return Take % (10**9 + 7)


def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[-1 for i in range(k + 1)] for i in range(n)]
    return f(0, k, arr, dp)
