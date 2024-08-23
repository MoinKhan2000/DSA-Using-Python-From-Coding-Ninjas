# Problem: Remove x from string
def removeX(str): 
    if len(str) == 0:
        return str
    smallOutput = removeX(str[1:])
    if str[0] == "x":
        return smallOutput
    else:
        return str[0] + smallOutput

# Main
string = input()
print(removeX(string))
