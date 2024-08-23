""" 
Does string 's' contain string 't' ?
Send Feedback
Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
Return true or false.
Do it recursively.
E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.
Input Format :
Line 1 : String s
Line 2 : String t
Output Format :
true or false
Sample Input 1 :
abchjsgsuohhdhyrikkknddg
coding
Sample Output 1 :
true
Sample Input 2 :
abcde
aeb
Sample Output 2 :
false


"""

import sys


def contains(s, t):
    len_of_s, len_of_t = len(s), len(t)
    spointer, tpointer = 0, 0

    while spointer < len_of_s and tpointer < len_of_t:
        if s[spointer] == t[tpointer]:
            tpointer += 1
        spointer += 1

    return tpointer == len_of_t


s = input()
t = input()

ans = contains(s, t)
if ans is True:
    print("true")
else:
    print("false")
sys.exit()
