temp = {}

# Using update method
temp.update([("Moin", 98), ("Harshit", 23)])
print(temp)
# {'Moin': 98, 'Harshit': 23}
temp.update([("Moin", 99)])
print(temp)
# {'Moin': 99, 'Harshit': 23}

del temp["Moin"]
print(temp)
# {'Harshit': 23}

temp["Moin"] = 99
print(temp)
# {'Harshit': 23, 'Moin': 99}
"""
del temp["Zara"]
print(temp)
# KeyError: 'Zara' and stopeed

"""
# print(temp.pop("Zara"))
# KeyError: 'Zara' and stopped

print(temp.pop("Moin"))  # This also update the original list
# 99

print(temp)

print(temp.__contains__("Moin"))
# False
print(temp.__contains__("Harshit"))
# True

temp.clear()
