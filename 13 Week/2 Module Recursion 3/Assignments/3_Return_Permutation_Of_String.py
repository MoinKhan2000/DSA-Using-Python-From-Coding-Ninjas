"""  
Return Permutations of a String
Send Feedback
Given a string, find and return all the possible permutations of the input string.
Note :
The order of permutations are not important.
Sample Input :
abc
Sample Output :
abc
acb
bac
bca
cab
cba
"""
from copy import deepcopy


def returnSubsetOfArray(arr, ind):
    if ind == len(arr):
        for el in arr:
            print(el, end="")
        print()
    for i in range(ind, len(arr)):
        arr[i], arr[ind] = arr[ind], arr[i]
        returnSubsetOfArray(arr, ind + 1)
        arr[i], arr[ind] = arr[ind], arr[i]


string = input()
lst = [el for el in string]

returnSubsetOfArray(lst, 0)
