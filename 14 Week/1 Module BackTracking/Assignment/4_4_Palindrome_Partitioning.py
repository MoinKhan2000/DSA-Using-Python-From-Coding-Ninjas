from sys import stdin
import json


def isPalindrome(s):
    return s == s[::-1]


def helper(s, ind, ans, temp):
    if ind == len(s):
        ans.append(temp.copy())
        return

    for i in range(ind, len(s)):
        if isPalindrome(s[ind : i + 1]):
            temp.append(s[ind : i + 1])
            helper(s, i + 1, ans, temp)
            temp.pop()


def partition(s):
    ans = []
    temp = []
    helper(s, 0, ans, temp)
    return ans


s = stdin.readline().rstrip()
final = partition(s)

for ele in final:
    ele = sorted(ele)
    print(json.dumps(ele))
