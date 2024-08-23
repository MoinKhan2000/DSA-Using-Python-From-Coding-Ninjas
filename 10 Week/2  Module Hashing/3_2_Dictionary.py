temp = {"Moin": 99, "Harshit": 98, "Harish": 97}
print(temp["Moin"])
print(temp["Harish"])
# print(temp["Zara"]) Throwing below error because key is not present
# Traceback (most recent call last):
#   File "d:\CN\2_DSA\10 Week\2  Module Hashing\3_2_Dictionary.py", line 4, in <module>
#     print(temp["Zara"])
# KeyError: 'Zara'

print(temp.get("Zara"))  # Doesn't throwing any error if the key is not present
# None


"""     We can explicitily provide what to return if the kye is not present     """
print(temp.get("Zara", 1))  # Return 1 if there is no key corresponding to Zara
# If the Zara doesn't exists then check for Mohsin if Mohsin doesn't go for Moin if Moin doesn't return 0
print(temp.get("Zara", temp.get("Mohsin", temp.get("Moin", 0))))
# print(
#     temp.get(
#         input("Enter student name to see the marks\n"), "Sorry student doesn't exists"
#     )
# )

# Getting the list of keys and list of values
keysOfTemp = temp.keys()
print(keysOfTemp)
# dict_keys(['Moin', 'Harshit', 'Harish'])
valuesOfTemp = temp.values()
print(valuesOfTemp)
# dict_values([99, 98, 97])

# Ways to print keys and it's values
# 1.
for key, value in zip(keysOfTemp, valuesOfTemp):
    print(key, value)

# 2.
print(temp.items())
for key, value in temp.items():
    print(key, value)

# 3.
for item in temp:
    print(item, temp[item])
