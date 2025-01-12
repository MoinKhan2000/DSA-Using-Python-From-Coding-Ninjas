""" 
Frog jump
Send Feedback
There is a frog on the '1st' step of an 'N' stairs long staircase. The frog wants to reach the 'Nth' stair. 'HEIGHT[i]' is the height of the '(i+1)th' stair.If Frog jumps from 'ith' to 'jth' stair, the energy lost in the jump is given by absolute value of ( HEIGHT[i-1] - HEIGHT[j-1] ). If the Frog is on 'ith' staircase, he can jump either to '(i+1)th' stair or to '(i+2)th' stair. Your task is to find the minimum total energy used by the frog to reach from '1st' stair to 'Nth' stair.
For Example
If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the total energy lost is 20.
Input Format:
The first line of the input contains an integer, 'T,’ denoting the number of test cases.

The first line of each test case contains a single integer,' N’, denoting the number of stairs in the staircase,

The next line contains ‘HEIGHT’ array.
Output Format:
For each test case, return an integer corresponding to the minimum energy lost to reach the last stair.
Note:
You do not need to print anything. It has already been taken care of. Just implement the given function.
Constraints:
1 <= T <= 10
1 <= N <= 100000.
1 <= HEIGHTS[i] <= 1000 .

Time limit: 1 sec
Sample Input 1:
2
4
10 20 30 10
3
10 50 10
Sample Output 1:
20
0
Explanation of sample input 1:
For the first test case,
The frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost).
Then a jump from the 2nd stair to the last stair (|10-20| = 10 energy lost).
So, the total energy lost is 20 which is the minimum. 
Hence, the answer is 20.

For the second test case:
The frog can jump from 1st stair to 3rd stair (|10-10| = 0 energy lost).
So, the total energy lost is 0 which is the minimum. 
Hence, the answer is 0.
Sample Input 2:
2
8
7 4 4 2 6 6 3 4 
6
4 8 3 10 4 4 
Sample Output 2:
7
2
"""
from typing import List

dp = []


def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1] * (n)

    def frogJumpHelper(n: int, heights: List[int]) -> int:
        if n == 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        left = frogJumpHelper(n - 1, heights) + abs(heights[n] - heights[n - 1])
        right = float("inf")
        if n > 1:
            right = frogJumpHelper(n - 2, heights) + abs(heights[n] - heights[n - 2])
        dp[n] = min(left, right)
        return min(left, right)

    return frogJumpHelper(n - 1, heights)


def frogJumpIterative(n: int, height: List[int]) -> int:
    if n == 0:
        return 0
    dp = [-1] * (n)
    dp[0] = 0
    for i in range(1, n):
        left = dp[i - 1] + abs(height[i] - height[i - 1])
        right = float("inf")
        if i > 1:
            right = dp[i - 2] + abs(height[i] - height[i - 2])
        dp[i] = min(left, right)
    return dp[n - 1]


def frogJumpOptimal(n: int, height) -> int:
    prev = 0
    prev2 = 0
    for i in range(1, n):
        fs = prev + abs(height[i] - height[i - 1])
        ss = float("inf")
        if i > 1:
            ss = prev2 + abs(height[i] - height[i - 2])
        curr = min(fs, ss)
        prev2 = prev
        prev = curr
    return prev


heights = [10, 20, 30, 10]
# heights = [7, 4, 4, 2, 6, 6, 3, 4]
n = len(heights)
min_cost = frogJumpOptimal(n, heights)
print(min_cost)

# heights = [10, 20, 30, 10]
# print(frogJump(4, heights))
