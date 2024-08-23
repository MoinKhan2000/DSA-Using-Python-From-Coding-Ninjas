""" 
Return subset of an array
Send Feedback
Given an integer array (of length n), find and return all the subsets of input array.
NOTE- Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.

Note :
The order of subsets are not important.


Input format :

Line 1 : Size of array

Line 2 : Array elements (separated by space)

Expected Time Complexity: O(2^N), where N is the size of given array
Sample Input:
3
15 20 12
Sample Output:
[] (this just represents an empty array, don't worry about the square brackets)
12 
20 
20 12 
15 
15 12 
15 20 
15 20 12 

"""

from copy import deepcopy


def returnSubsetOfArray(arr, output):
    if len(arr) == 0:
        for el in output:
            print(el, end=" ")
        print()
        return
    output1 = deepcopy(output)
    output2 = deepcopy(output)
    output2.append(arr[0])
    returnSubsetOfArray(arr[1:], output1)
    returnSubsetOfArray(arr[1:], output2)


n = input()
lst = [int(x) for x in input().split() if x]
returnSubsetOfArray(lst, [])
