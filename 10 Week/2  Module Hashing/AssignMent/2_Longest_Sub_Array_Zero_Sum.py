""" 
Longest subarray zero sum
Send Feedback
Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.
Input Format:
The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
The following line contains N space separated integers, that denote the value of the elements of the array.
Output Format
The first and only line of output contains length of the longest subarray whose sum is zero.
Constraints:
0 <= N <= 10^8
Time Limit: 1 sec
Sample Input 1:
10 
 95 -97 -387 -435 -5 -70 897 127 23 284
Sample Output 1:
5
Explanation:
The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897 
Note
You don't have to print anything. Just complete the definition of the function given and return the value accordingly.
"""
from os import *
from sys import *
from collections import *
from math import *
from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)

# Not done
# def maxSumArrayThatSumToK(nums, n, K):
#     if not nums:
#         return 0
#     max_sum = current_sum = 0
#     prefix_sum = {0: -1}
#     for i in range(n):
#         current_sum += nums[i]
#         if current_sum - K in prefix_sum:
#             max_sum = max(max_sum, i - prefix_sum[current_sum - K])
#         if current_sum not in prefix_sum:
#             prefix_sum[current_sum] = i
#     print(prefix_sum)
#     return max_sum


def getLongestSubarray(arr: [int], n: int) -> int:
    maxLen = 0
    hashSet = {}
    curLength = 0
    totalSum = 0
    for i in range(len(arr)):
        totalSum += arr[i]
        if totalSum == n:
            maxLen = max(maxLen, i + 1)
        remain = totalSum - n
        if remain in hashSet:
            curLength = i - hashSet[remain]
            maxLen = max(curLength, maxLen)
        if totalSum not in hashSet:
            hashSet[totalSum] = i
    return maxLen


def subsetSum(arr):
    dictionary = {}
    currentSum = 0
    for i in range(len(arr)):
        currentSum += arr[i]
        if currentSum not in dictionary:
            dictionary[currentSum] = i
        else:
            dictionary[currentSum] = i
        if currentSum == 0:
            dictionary[currentSum] = i
    return dictionary.get(0, 0) + 1


# Taking input using fast I/O
def takeInput():
    n = int(input())
    if n == 0:
        return list(), n
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


arr, n = takeInput()
print(subsetSum(arr))
