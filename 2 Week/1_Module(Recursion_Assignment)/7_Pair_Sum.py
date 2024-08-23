"""   
Pair Star
Send Feedback
Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
Input format :
String S
Output format :
Modified string
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
hello
Sample Output 1:
hel*lo
Sample Input 2 :
aaaa
Sample Output 2 :
a*a*a*a

"""


def pairStars(str):
    if len(str) == 0:
        return
    if len(str) == 1:
        print(str[0], end="")
    elif str[0] == str[1]:
        print(str[0], end="*")
        pairStars(str[1:])
    else:
        print(str[0], end="")
        pairStars(str[1:])


str = input()
pairStars(str)
