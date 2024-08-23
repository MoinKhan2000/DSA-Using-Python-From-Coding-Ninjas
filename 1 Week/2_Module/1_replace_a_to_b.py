def replace_a_to_b(str, a, b):
    if len(str) == 0:
        return str
    smallOutput = replace_a_to_b(str[1:], a, b)
    if str[0] == "a":
        return b + smallOutput
    else:
        return str[0] + smallOutput


string = "ababab"
output = replace_a_to_b(string, "a", "b")
print(output)


def replace_a_to_b_and_b_to_a(str, a, b):
    if len(str) == 0:
        return str
    smallOutput = replace_a_to_b_and_b_to_a(str[1:], a, b)
    if str[0] == "a":
        return b + smallOutput
    else:
        return a + smallOutput


string = "ababab"
output = replace_a_to_b_and_b_to_a(string, "a", "b")
print(output)
