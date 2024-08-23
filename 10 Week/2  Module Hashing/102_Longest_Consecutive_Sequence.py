""" 
Longest Consecutive Sequence
Send Feedback
You are given an unsorted array/list 'ARR' of 'N' integers. Your task is to return the length of the longest consecutive sequence.
The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2, ..., 'NUM' + L] where 'NUM' is the starting integer of the sequence and 'L' + 1 is the length of the sequence.
Note:
If there are any duplicates in the given array we will count only one of them in the consecutive sequence.
For example-
For the given 'ARR' [9,5,4,9,10,10,6].

Output = 3
The longest consecutive sequence is [4,5,6].
Follow Up:
Can you solve this in O(N) time and O(N) space complexity?
Input format :
The first line of input contains a single integer 'T', representing the number of test cases or queries to be run. Then the 'T' test cases follow.

The first line of each test case contains integer 'N' denoting the size of the array.

The second line of each test case contains 'N' single space-separated integers, elements of the array.  
Output format :
For each test case, print an integer in a single line that represents the length of the longest consecutive sequence.
Note :
You are not required to print the expected output; it has already been taken care of. Just implement the function. 
Constraints :
1 <= T <= 10
1 <= N <= 10^5
-10^9 <= ARR[i] <= 10^9

Time Limit: 1 sec
Sample Input 1 :
1 
5
33 20 34 30 35
Sample Output 1 :
3
Explanation to Sample Input 1 :
The longest consecutive sequence is [33, 34, 35].
Sample Input 2 :
1
7
1 9 3 10 4 20 2    
Sample Output 2 :
4
Explanation to Sample Input 2 :
The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2,...,'NUM' + 'L']. So in the given array, the longest consecutive sequence is [1,2,3,4] where 'NUM' = 1 and 'L' = 3. And the length of the sequence will be 'L' + 1 = 4.
"""
from math import *
from collections import *
from sys import *
from os import *


def LongestSubarrayThatSumToKBruteForce(arr, n):
    longLenth = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == n:
                longLenth = max(longLenth, j - i + 1)
    return longLenth


def lengthOfLongestConsecutiveSequence(arr, n):
    if n == 0:
        return 0
    element_set = set(arr)
    max_length = 1
    for num in element_set:
        if num - 1 not in element_set:
            current_num = num
            current_length = 1
            while current_num + 1 in element_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length


def maxSumArrayThatSumToK(nums, K):
    n = len(nums)
    if not nums:
        return 0
    max_sum = current_sum = 0
    prefix_sum = {0: -1}
    for i in range(n):
        current_sum += nums[i]
        if current_sum - K in prefix_sum:
            max_sum = max(max_sum, i - prefix_sum[current_sum - K])
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i
    return max_sum


# Below code will not work 0 present in the array
def longestSequeceThatSumToKUsingHash(arr, n):
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
        hashSet[totalSum] = i
    return maxLen


# Always work for 0 as well as for negative elements
def longestSequeceThatSumToKUsingHashWorkFor0(arr, n):
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


def longestSequeceThatSumToKUsingSlidingWindow(arr, n):
    left = 0
    right = 0
    sum = arr[0]
    maxLen = 0
    while right < len(arr):
        while left <= right and sum > n:
            sum -= arr[left]
            left += 1
        if sum == n:
            maxLen = max(right - left + 1, maxLen)
        right += 1
        if right < len(arr):
            sum += arr[right]
    return maxLen


def longestSequence(arr, n):
    if n == 0:
        return 0
    longest = 1
    st = set(arr)
    for it in st:
        if it - 1 not in st:
            count = 1
            x = it
            while x + 1 in st:
                x += 1
                count += 1
            longest = max(longest, count)
    return longest


arr = [1, 4, -1, 1, -1, 4]
arr = [2, 0, 0, 3]
arr = [1, 2, 3, 1, 1, 1, 1, 3, 3]
arr = [1, 2, 1, 3]
n = 2
arr = [95, -97, -387, -435, -5, -70, 897, 127, 23, 284]
n = 0
print(LongestSubarrayThatSumToKBruteForce(arr, n))
# Below function will not work for 0
print(longestSequeceThatSumToKUsingHash(arr, n))
# Below funciton will work for 0 also
print(longestSequeceThatSumToKUsingHashWorkFor0(arr, n))
print(longestSequeceThatSumToKUsingSlidingWindow(arr, n))
