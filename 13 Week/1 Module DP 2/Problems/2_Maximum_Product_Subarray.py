"""
Maximum Product Subarray
Send Feedback
You are given an array “arr'' of integers. Your task is to find the contiguous subarray within the array which has the largest product of its elements. You have to report this maximum product.
An array c is a subarray of array d if c can be obtained from d by deletion of several elements from the beginning and several elements from the end.

For e.g.- The non-empty subarrays of an array [1,2,3] will be- [1],[2],[3],[1,2],[2,3],[1,2,3]. 
For Example:
If arr = {-3,4,5}.
All the possible non-empty contiguous subarrays of “arr” are {-3}, {4}, {5}, {-3,4}, {4,5} and {-3,4,5}.
The product of these subarrays are -3, 4, 5, -12, 20 and -60 respectively.
The maximum product is 20. Hence, the answer is 20.
Follow Up:
Can you solve this in linear time and constant space complexity?
Input format:
The first line contains an integer 'T' which denotes the number of test cases or queries to be run. Then, the T test cases follow.
The first line of each test case contains a single integer N, denoting the number of elements of the array “arr”.
The second line of each test case contains N space separated integers denoting the elements of the array “arr”.
Output format:
For each test case, print the maximum product of the contiguous non-empty subarray of the array “arr”.

Output for each test case will be printed in a separate line.
Note:
You do not need to print anything. It has already been taken care of. Just implement the given function.
Constraints:
1 <= T <= 100
1 <= N <= 5000
-100 <= arr[i] <= 100
where N is the size of the array “arr”.

Time limit: 1 second
Sample Input 1:
2
4
3 5 -2 -4
5
2 4 3 5 6
Sample Output 1:
120
720
Explanation for sample 1:
For the first test case, all the possible non-empty contiguous subarrays of “arr” are {3}, {5}, {-2}, {-4}, {3,5}, {5,-2}, {-2,-4}, {3,5,-2}, {5,-2,-4} and {3,5,-2,-4}. 
The product of these subarrays are 3, 5, -2, -4, 15, -10, 8, -30, 40 and 120 respectively.
So, the maximum product is 120.
For the second test case, since all the elements in the array “arr” are positive, we get the maximum product subarray by multiplying all the elements in the array. So, the maximum product is 720.
Sample Input 2:
2
4
6 0 2 -4
3
-1 -3 -4
Sample Output 2:
6
12

"""
from os import *
from sys import *
from collections import *
from math import *


def maximumProduct(arr, n):
    if n == 0:
        return 0

    pre = 1
    suff = 1
    ans = float("-inf")

    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1

        pre *= arr[i]
        suff *= arr[n - i - 1]

        ans = max(ans, pre, suff)

    return ans
