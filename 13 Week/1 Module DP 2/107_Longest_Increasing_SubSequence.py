"""Longest Increasing Subsequence
Send Feedback
For a given array with N elements, you need to find the length of the longest subsequence from the array such that all the elements of the subsequence are sorted in strictly increasing order.
Strictly Increasing Sequence is when each term in the sequence is larger than the preceding term.
For example:
[1, 2, 3, 4] is a strictly increasing array, while [2, 1, 4, 3] is not.
Input format:
The first line of input contains an integer 'N', representing the size of the array.

The second line of input contains 'N' space-separated integers, representing the elements of the array.
Output Format:
The only output line contains one integer representing the length of the longest increasing subsequence.
Note:
You do not need to print anything; it has already been taken care of. Just implement the given functions.
Input Constraints
1 <= N <= 10^5
-10^5 <= element <= 10^5

Time Limit: 1sec
Sample Input :
6
5 4 11 1 16 8
Sample Output 1 :
3
Explanation of Sample Input 1:
Length of longest subsequence is 3 i.e. [5, 11, 16] or [4, 11, 16].
Sample Input 2:
3
1 2 2
Sample Output 2 :
2"""

from sys import stdin
import sys

sys.setrecursionlimit(10**7)


def longestIncreasingSubsequence(arr, n):
    if n == 0:
        return 0

    tails = [0] * n
    size = 1
    tails[0] = arr[0]

    for i in range(1, n):
        if arr[i] < tails[0]:
            tails[0] = arr[i]
        elif arr[i] > tails[size - 1]:
            tails[size] = arr[i]
            size += 1
        else:
            # Find the smallest element in tails which is greater than or equal to arr[i]
            left, right = 0, size - 1
            while left < right:
                mid = (left + right) // 2
                if tails[mid] >= arr[i]:
                    right = mid
                else:
                    left = mid + 1

            tails[left] = arr[i]

    return size


# taking inpit using fast I/O
def takeInput():
    n = int(input())

    if n == 0:
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


# main
arr, n = takeInput()
print(longestIncreasingSubsequence(arr, n))
