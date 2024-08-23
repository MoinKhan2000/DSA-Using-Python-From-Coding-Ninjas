"""  
Check Palindrome (recursive)
Send Feedback
Check whether a given String 'S' is a palindrome using recursion.


Return true or false.


Note:
You don’t need to print anything. Just implement the given function.
Example:
Input: s = "racecar"
Output: true
Explanation: "racecar" is a palindrome.
Input Format:
The first and only line of the input contains string S.
Output format:
Return a boolean value True or False.
Sample Input 1:
abbba
Sample Output 1:
true
Explanation Of Sample Input 1 :
“abbba” is a palindrome
Sample Input 2:
abcd
Sample Output 2:
false
Explanation Of Sample Input 2 :
“abcd” is not a palindrome.
Constraints:
0 <= |S| <= 10^6
where |S| represents the length of string S.

"""


import sys

def isPalindromeRecursive(string: str, left, right) -> bool:
    if left >= right:
        return True
    elif string[left] == string[right]:
        return isPalindromeRecursive(string, left + 1, right - 1)
    else:
        return False


def isPalindrome(string: str) -> bool:
    return isPalindromeRecursive(string, 0, len(string) - 1)

sys.setrecursionlimit(10**6);

a = input()
if len(a)>=1:
    result = isPalindrome(a)
    if result == True:
        print("true")
    else:
        print("false")
else:
    print('false');

sys.exit()
