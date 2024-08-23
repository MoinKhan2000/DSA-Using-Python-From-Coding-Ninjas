def firstIndexOfElementRecursive(lst, num):
    if len(lst) == 0:
        return -1

    if lst[0] == num:
        return 0
    smallOutput = firstIndexOfElementRecursive(lst[1:], num)
    # print(lst)
    # if smallOutput == -1:
    #     return smallOutput
    # else:
    #     return 1 + smallOutput
    if smallOutput >= 0:
        return 1 + smallOutput
    else:
        return smallOutput


num = int(input())
n = [int(x) for x in input().split(" ")]
digit = int(input())
print(firstIndexOfElementRecursive(n, digit))
