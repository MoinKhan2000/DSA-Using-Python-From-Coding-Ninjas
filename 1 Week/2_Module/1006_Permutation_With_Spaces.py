def permutaionWithSpaces(string, output):
    if len(string) == 0:
        print(output)
        return
    output1 = output
    output2 = output
    output1 += " " + string[0]
    output2 += string[0]
    string = string[1:]
    permutaionWithSpaces(string, output1)
    permutaionWithSpaces(string, output2)


str = input()
output = str[0]
permutaionWithSpaces(str[1:], output)

