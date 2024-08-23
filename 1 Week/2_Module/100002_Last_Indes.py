def lastIndexOfElementRecursive(lst, num):
    if len(lst) == 0:
        return -1
    smallOutput = lastIndexOfElementRecursive(lst[1:], num)
    if smallOutput != -1:
        return 1 + smallOutput
    else:
        if lst[0] == num:
            return 0
        else:
            return -1


lst = [9, 8, 10, 8]
print(lastIndexOfElementRecursive(lst, 8))
