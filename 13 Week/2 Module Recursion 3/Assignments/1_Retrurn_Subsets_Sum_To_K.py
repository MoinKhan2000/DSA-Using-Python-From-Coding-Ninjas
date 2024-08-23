""" 
Return subsets sum to K
Send Feedback
Given an array A of size n and an integer K, return all subsets of A which sum to K.
Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.


Note :
The order of subsets are not important.


Input format :
Line 1 : Integer n, Size of input array
Line 2 : Array elements separated by space
Line 3 : K 
Constraints :
1 <= n <= 20
Sample Input :
9 
5 12 3 17 1 18 15 3 17 
6
Sample Output :
3 3
5 1

"""
import sys

sys.setrecursionlimit(10**8)

from copy import deepcopy


def subsetsSumK(arr, k):
    def returnSubsetOfArray(arr, output):
        if len(arr) == 0:
            if sum(output) == k:
                for el in output:
                    print(el, end=" ")
                print()
            return
        output1 = output.copy()
        output2 = output.copy()
        output2.append(arr[0])
        returnSubsetOfArray(arr[1:], output1)
        returnSubsetOfArray(arr[1:], output2)

    liOfLi = []
    returnSubsetOfArray(arr, [])
    return liOfLi


# taking input from command line arguments


n = input()
lst = [int(x) for x in input().split() if x]
k = input()
k = int(k)
subsetsSumK(lst, k)
