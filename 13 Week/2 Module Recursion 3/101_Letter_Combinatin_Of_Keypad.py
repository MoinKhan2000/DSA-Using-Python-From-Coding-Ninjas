def keypad(n):
    if n == 0:
        output = []
        output.append("")
        return output
    smallerNumber = n // 10
    lastDig = n % 10
    smallerOutput = keypad(smallerNumber)
    stringForLastDigit = getKeyString(lastDig)
    output = []
    for s in smallerOutput:
        for c in stringForLastDigit:
            output.append(s + c)

    return output


def getKeyString(ind):
    keypad_mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    return keypad_mapping[str(ind)]


ans = keypad(23)
for el in ans:
    print(el)
