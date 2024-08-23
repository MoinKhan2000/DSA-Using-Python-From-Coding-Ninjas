# ip='a1b2'
# op= a1b2 a1B2 A1B2 A1b2
import sys


def subsetRecursive(string, output, subSet):
    if len(string) == 0:
        subSet.append(output)
        return 1
    output1 = output
    output2 = output
    if string[0].isnumeric():
        output2 += string[0]
        subsetRecursive(string[1:], output2, subSet)
    else:
        output1 += string[0].capitalize()
        output2 += string[0].lower()
        subsetRecursive(string[1:], output1, subSet)
        subsetRecursive(string[1:], output2, subSet)
    return


num = int(input())
for i in range(num):
    str = input()
    if str.isnumeric():
        print(str)
    else:
        subSet = []
        subsetRecursive(str, "", subSet)
        subSet = set(subSet)
        for el in subSet:
            print(el, end=" ")
        subSet = []
        print()

sys.exit()
