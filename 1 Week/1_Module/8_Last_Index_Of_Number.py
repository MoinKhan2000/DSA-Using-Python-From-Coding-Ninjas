# def lastIndex(lst, x):
#     l = len(lst)
#     if l == 0:
#         return -1
#     smallerList = lst[1:]
#     smallerListOutput = lastIndex(smallerList, x)
#     if smallerListOutput != -1:
#         return smallerListOutput + 1
#     else:
#         if lst[0] == x:
#             return 0
#         else:
#             return -1
# a = [1, 2, 3, 4, 8, 12, 142, 2, 2, 2]
# print(lastIndex(a, 2))


def lastIndex(lst, x, index):
    lenOfList = len(lst)
    if index == lenOfList:
        return -1
    smallListOutput = lastIndex(lst, x, index + 1)
    if smallListOutput != -1:
        return smallListOutput
    else:
        if lst[index] == x:
            return index
        else:
            return -1


a = [1, 2, 3, 4, 8, 12, 142, 2, 2, 2]
print(lastIndex(a, 2, 0))
