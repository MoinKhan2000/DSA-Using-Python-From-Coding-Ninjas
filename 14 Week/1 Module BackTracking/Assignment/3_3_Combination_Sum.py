""" 
Combination Sum
Send Feedback
You are given an array 'ARR' of 'N' distinct positive integers. You are also given a non-negative integer 'B'.


Your task is to return all unique combinations in the array whose sum equals 'B'. A number can be chosen any number of times from the array 'ARR'.


Elements in each combination must be in non-decreasing order.


For example:
Let the array 'ARR' be [1, 2, 3] and 'B' = 5. Then all possible valid combinations are-

(1, 1, 1, 1, 1)
(1, 1, 1, 2)
(1, 1, 3)
(1, 2, 2)
(2, 3)
Input Format
Then the first line contains two space-separated integers, 'N' and 'B', denoting the number of elements in the array and the target sum, respectively.
The second line of each test case contains 'N' space-separated integers representing the elements of the array 'ARR'.
Output Format :
The only line will contain 'Yes', if the answer is correct. Else, it will contain 'No'.
Note:
You do not need to print anything; it has already been taken care of. Just implement the given function.
Sample Input 1 :
3 8
2 3 5
Sample Output 1:
Yes
Explanation Of Sample Input 1 :
All possible valid combinations are:
2 2 2 2
2 3 3
3 5
Sample Input 2 :
3 5
1 2 3 
Sample Output 2:
Yes
Constraints:
1 <= 'N' <= 15
1 <= 'B' <= 20
1 <= 'ARR[i]' <= 20

Time Limit: 1sec
"""


from copy import copy
from copy import deepcopy

# import deepcodpy


def findCombinations(index, target, arr, ans, temp):
    # base case
    if index == len(arr):
        if target == 0:
            ans.append(temp.copy())
        return
    if arr[index] <= target:
        temp.append(arr[index])
        findCombinations(index, target - arr[index], arr, ans, temp)
        temp.pop()

    findCombinations(index + 1, target, arr, ans, temp)


def combSum(arr, target):
    arr.sort()
    temp = []
    ans = []
    findCombinations(0, target, arr, ans, temp)
    return ans


arr = [1, 2, 3]
b = 4
print("Output:", combSum(arr, b))
