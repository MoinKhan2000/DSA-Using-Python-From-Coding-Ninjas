""" 
House Robber
Send Feedback
Mr. X is a professional robber planning to rob houses along a street. Each house has a certain amount of money hidden. All houses along this street are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
You are given an array/list of non-negative integers 'ARR' representing the amount of money of each house. Your task is to return the maximum amount of money Mr. X can rob tonight without alerting the police.
Note:
It is possible for Mr. X to rob the same amount of money by looting two different sets of houses. Just print the maximum possible robbed amount, irrespective of sets of houses robbed.
For example:
(i) Given the input array arr[] = {2, 3, 2} the output will be 3 because Mr X cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses. So, he’ll rob only house 2 (money = 3)

(ii) Given the input array arr[] = {1, 2, 3, 1} the output will be 4 because Mr X rob house 1 (money = 1) and then rob house 3 (money = 3).

(iii) Given the input array arr[] = {0} the output will be 0 because Mr. X has got nothing to rob.
Input Format :
The first line of input contains an integer 'T' representing the number of the test case. Then the test case follows.

The first line of each test case contains an integer, ‘N’ representing the size of the first array/list.

The second line of each test case contains 'N' single space-separated integers representing the array/list elements.
Output Format :
For each test case, print a single line containing a single integer denoting the maximum money that can be robbed in a separate line.

The output of each test case will be printed in a separate line.
Note:
You do not need to print anything; it has already been taken care of. Just implement the given function.
Constraints:
1 <= T <= 10
1 <= N <= 5 x 10 ^ 3
1 <= ARR[i] <= 10 ^ 9

Time limit: 1 sec.
Sample Input 1:
3
1
0
3
2 3 2
4
1 3 2 1
Sample Output 1:
0
3
4
Explanation of Input 1:
(i) Mr. X has only one house to rob, but with no money.

(ii) Mr. X cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses (remember, it’s a circular street). So, he’ll rob only house 2 (money = 3) with a maximum value

(iii) Mr. X will get maximum value when he robs house 2 (money = 3) and then robs house 4 (money = 1) i.e. 4 units of money.
Sample Input 2:
3
5
1 5 1 2 6
3
2 3 5
4
1 3 2 0
Sample Output 2:
11
5
3
"""

from os import *
from sys import *
from collections import *
from math import *


def maximumNonAdjacentSum(nums):
    dp = [-1] * len(nums)

    def maximumSumOptimal(n):
        prev1 = nums[0]
        prev2 = 0
        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick = nums[i] + prev2
            notPick = prev1
            curr = max(pick, notPick)
            prev2 = prev1
            prev1 = curr
        return curr

    length = len(nums)
    return maximumSumOptimal(length)


def houseRobber(valueInHouse):
    if len(valueInHouse) == 1:
        return valueInHouse[0]
    # temp1 = []
    # temp2 = []
    # for i in range(len(valueInHouse)):
    #     if i != 0:
    #         temp1.append(valueInHouse[i])
    #     if i != len(valueInHouse) - 1:
    #         temp2.append(valueInHouse[i])
    ans1 = maximumNonAdjacentSum(valueInHouse[: len(valueInHouse) - 1])
    ans2 = maximumNonAdjacentSum(valueInHouse[1:])

    return max(ans1, ans2)


arr = [1, 5, 1, 2, 6]
arr = [2, 3, 5]
arr = [2, 7, 9, 3, 1]
print(houseRobber(arr))

dp = [[-1 for j in range(4)] for i in range(4)]
print(dp)
# printing dp matrix as a matrix
for el in dp:
    for li in el:
        print(li, end=" ")
    print("")
