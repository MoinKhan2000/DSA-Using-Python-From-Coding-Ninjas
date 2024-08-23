import sys


def generateBalancedParenthesis(open, closed, str, valid_combinations):
    if open == 0 and closed == 0:
        valid_combinations.append(str)
        return

    if open > 0:
        op1 = str + "("
        generateBalancedParenthesis(open - 1, closed, op1, valid_combinations)
    if closed > open:
        op2 = str + ")"
        generateBalancedParenthesis(open, closed - 1, op2, valid_combinations)


def validParenthesis(n: int) -> int:
    valid_combinations = []
    generateBalancedParenthesis(n, n, "", valid_combinations)
    return valid_combinations


# num = [int(x) for x in input().split(" ")]
# num.sort
# for el in num:
#     combinations = validParenthesis(el)
#     for combination in combinations:
#         print(combination, end=" ")
num = int(input())
for i in range(0, num):
    n = int(input())
    combinations = validParenthesis(n)
    for combination in combinations:
        print(combination, end=" ")
    print()

sys.exit()
