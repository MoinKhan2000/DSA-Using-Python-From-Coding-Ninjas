""" 
Split Array
Send Feedback
Given an integer array A of size N, check if the input array can be divided in two groups G1 and G2 with following properties-
- Sum of both group elements are equal
- Group 1: All elements in the input, which are divisible by 5 
- Group 2: All elements in the input, which are divisible by 3 (but not divisible by 5). 
- Elements which are neither divisible by 5 nor by 3, can be put in either group G1 or G2 to satisfy the equal sum property. 
Group 1 and Group 2 are allowed to be unordered and all the elements in the Array A must belong to only one of the groups.


Return true, if array can be split according to the above rules, else return false.
Note: You will get marks only if all the test cases are passed.
Input Format :
Line 1 : Integer N (size of array)
Line 2 : Array A elements (separated by space)
Output Format :
true or false
Constraints :
1 <= N <= 50
Sample Input 1 :
2
1 2
Sample Output 1 :
false
Sample Input 2 :
3
1 4 3
Sample Output 2 :
true


"""

import sys


def split(arr, i, sumOfG1):
    if i == len(arr):
        return sum(arr) - sumOfG1 == sumOfG1

    if arr[i] % 5 == 0:
        return split(arr, i + 1, sumOfG1 + arr[i])

    if arr[i] % 3 == 0:
        return split(arr, i + 1, sumOfG1)

    return split(arr, i + 1, sumOfG1 + arr[i]) or split(arr, i + 1, sumOfG1)


n = int(input())
arr = list(map(int, input().split()))

result = split(arr, 0, 0)

if result:
    print("true")
else:
    print("false")

sys.exit()
