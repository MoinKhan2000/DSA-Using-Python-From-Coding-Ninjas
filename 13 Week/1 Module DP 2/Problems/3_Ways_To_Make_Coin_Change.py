""" 
Ways To Make Coin Change
Send Feedback
You are given an infinite supply of coins of each of denominations D = {D0, D1, D2, D3, ...... Dn-1}. You need to figure out the total number of ways W, in which you can make a change for value V using coins of denominations from D. Print 0, if a change isn't possible.
Input Format
The first line of input contains an integer N, representing the total number of denominations.

The second line of input contains N integers values separated by a single space. Each integer value represents the denomination value.

The third line of input contains the value of V, representing the value for which the change needs to be generated.
Output Format:
For each test case, print an integer denoting the total number of ways W, in which a change for V is possible.
Note:
You do not need to print anything, it has already been taken care of. Just implement the given function.
Constraints :
1 <= N <= 10
1 <= D[i] <=10^5
1 <= V <= 2 * 10^3

Where 'D[i]' represent the value of ith denomination. 

Time Limit: 1sec
Sample Input 1 :
3
1 2 3
4
Sample Output 1:
4
Explanation for Sample Output 1:
We can make a change for the value V = 4 in four ways.
1. (1,1,1,1), 
2. (1,1, 2), [One thing to note here is, (1, 1, 2) is same as that of (2, 1, 1) and (1, 2, 1)]
3. (1, 3), and 
4. (2, 2)
Sample Input 2 :
3
5 3 2
1
Sample Output 2:
0

"""

from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


def countWaysToMakeChange(denominations, value):
    # Your code goes here
    n = len(denominations)
    dp = [[0 for _ in range(value + 1)] for _ in range(n)]
    prev = [0 for _ in range(value + 1)]
    curr = [0 for _ in range(value + 1)]
    for T in range(value + 1):
        prev[T] = 1 if T % denominations[0] == 0 else 0
    for ind in range(1, n):
        for T in range(value + 1):
            notTake = prev[T]
            take = 0
            if denominations[ind] <= T:
                take = curr[T - denominations[ind]]
            curr[T] = take + notTake
        prev = curr.copy()
    return prev[value]


# taking inpit using fast I/O
def takeInput():
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


# main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))
