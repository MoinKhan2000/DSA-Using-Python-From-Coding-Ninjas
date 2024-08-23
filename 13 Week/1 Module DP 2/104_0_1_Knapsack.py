"""  
0 1 Knapsack
Send Feedback
A thief is robbing a store and can carry a maximal weight of W into his knapsack. There are N items and the ith item weighs wi and is of value vi. Considering the constraints of the maximum weight that a knapsack can carry, you have to find and return the maximum value that a thief can generate by stealing items.
Input Format:
The first line contains a single integer T representing the number of test cases.      
The T-test cases are as follows:

Line 1:The first line contains an integer, that denotes the value of N. 
Line 2:The following line contains N space-separated integers, that denote the values of the weight of items. 
Line 3:The following line contains N space-separated integers, that denote the values associated with the items. 
Line 4:The following line contains an integer that denotes the value of W. W denotes the maximum weight that a thief can carry.
Output Format :
The first and only line of output contains the maximum value that a thief can generate, as described in the task. 
The output of every test case is printed in a separate line.
Constraints:
1 <= T <= 10
1 <= N <= 10^2
1<= wi <= 50
1 <= vi <= 10^2
1 <= W <= 10^3

Time Limit: 1 second
Follow Up:
Can we solve this using space complexity of not more than O(W)?
Sample Input:
1 
4
1 2 4 5
5 4 8 6
5
Sample Output:
13
"""

import sys


def knapsack(N, wt, val, W):
    prev = [0 for _ in range(W + 1)]
    curr = [0 for _ in range(W + 1)]

    n = len(val)

    for w in range(wt[0], W + 1):
        prev[w] = val[0]

    for ind in range(1, n):
        for w in range(0, W + 1):
            notTaken = prev[w]
            take = float("-inf")
            if wt[ind] <= w:
                take = prev[w - wt[ind]] + val[ind]
            curr[w] = max(notTaken, take)
        prev = curr.copy()
    return prev[W]


t = int(input())
while t > 0:
    t -= 1
    N = int(input())
    weights = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    W = int(input())
    print(knapsack(N, weights, values, W))

sys.exit()
