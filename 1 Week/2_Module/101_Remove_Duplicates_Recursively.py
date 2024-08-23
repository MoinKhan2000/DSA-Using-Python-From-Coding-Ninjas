# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    if len(string) == 0 or len(string) == 1:
        return string
    elif string[0] == string[1]:
        smallerOutput = removeConsecutiveDuplicates(string[1:])
        return smallerOutput
    else:
        smallerOutput = removeConsecutiveDuplicates(string[1:])
        return string[0] + smallerOutput


# # Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
