# Problem: Remove x from string
def replacePi(str):
    if len(str) == 0 or len(str) == 1:
        return str
    if str[0] == "p" and str[1] == "i":
        smallOutput = replacePi(str[2:])
        return "3.14" + smallOutput
    else:
        smallOutput = replacePi(str[1:])
        return str[0] + smallOutput


# Main
string = input()
print(replacePi(string))
